import json
from .event import StreamEvent
from .stream_connection import StreamConnection, LOGIN_STREAM_ID
from .stream_cxn_state import StreamCxnState
from ..._core.session import SessionCxnType
from ...usage_collection import StreamUsageKey


class OMMStreamConnection(StreamConnection):
    @property
    def subprotocol(self) -> str:
        return "tr_json2"

    def get_login_message(self):
        dacs_params = self._session._dacs_params
        access_token = self._session._access_token

        key = {"Elements": {}}
        if self._session._get_session_cxn_type() == SessionCxnType.DESKTOP:
            key["Elements"]["AppKey"] = self._session.app_key
            key["Elements"]["Authorization"] = f"Bearer {access_token}"
        elif self._session._get_session_cxn_type() in {
            SessionCxnType.REFINITIV_DATA_AND_DEPLOYED,
            SessionCxnType.DEPLOYED,
        }:
            key["Name"] = dacs_params.deployed_platform_username
        else:  # otherwise it can only be RefinitivDataConnection instance
            key["NameType"] = "AuthnToken"
            if access_token:
                key["Elements"]["AuthenticationToken"] = access_token

        ####

        key["Elements"]["ApplicationId"] = dacs_params.dacs_application_id
        key["Elements"]["Position"] = dacs_params.dacs_position or "/".join(self._get_socket_info())

        login_message = {
            "Domain": "Login",
            "ID": LOGIN_STREAM_ID,
            "Key": key,
        }
        return login_message

    def get_close_message(self) -> dict:
        close_message = {
            "Domain": "Login",
            "ID": LOGIN_STREAM_ID,
            "Type": "Close",
        }
        return close_message

    def _handle_login_message(self, message: dict):
        """
        Parameters
        ----------
        message
            {
                'ID': 2,
                'Type': 'Refresh',
                'Domain': 'Login',
                'Key':
                    {
                        'Name': TOKEN_HERE,
                        'Elements': {
                            'AllowSuspectData': 1, 'ApplicationId': '256',
                            'ApplicationName': 'RTO',
                            'AuthenticationErrorCode': 0,
                            'AuthenticationErrorText': {
                                'Type': 'AsciiString', 'Data': None
                            },
                            'AuthenticationTTReissue': 1634562361,
                            'Position': '10.46.188.21/EPUAKYIW3629',
                            'ProvidePermissionExpressions': 1,
                            'ProvidePermissionProfile': 0,
                            'SingleOpen': 1, 'SupportEnhancedSymbolList': 1,
                            'SupportOMMPost': 1,
                            'SupportPauseResume': 0, 'SupportStandby': 0,
                            'SupportBatchRequests': 7,
                            'SupportViewRequests': 1, 'SupportOptimizedPauseResume': 0
                        }
                    },
                'State':
                    {
                        'Stream': 'Open', 'Data': 'Ok',
                        'Text': 'Login accepted by host ads-fanout-lrg-az2-apse1-prd.'
                    }, 'Elements': {'PingTimeout': 30, 'MaxMsgSize': 61426}
            }
        """

        state = message.get("State", {})
        stream_state = state.get("Stream")

        if stream_state == "Open":
            self._state = StreamCxnState.MessageProcessing
            self._connection_result_ready.set()

        elif stream_state == "Closed":
            self.debug(f"{self._classname} received a closing message: state={self.state}, message={message}")
            self._state = StreamCxnState.Disconnected
            not self.can_reconnect and self._connection_result_ready.set()
            self._config.info_not_available()
            self._listener.close()

        else:
            state_code = state.get("Code", "")
            text = state.get("Text", "")

            if "Login Rejected." in text or state_code == "UserUnknownToPermSys":
                self._config.info_not_available()
                self._listener.close()

                if not self.can_reconnect:
                    self.debug(f"Connection error: {message}")
                    self._state = StreamCxnState.Disconnected
                    self._connection_result_ready.set()

            else:
                raise ValueError(
                    f"{self._classname}._handle_login_message() | "
                    f"Don't know what to do state={self.state}, message={message}"
                )

    def _update_usage_counter(self, stream_id: int, key: dict, message_type: str):
        usage_key = StreamUsageKey(stream_id, key.get("Service"), key.get("Name"))
        self.usage_counter[usage_key][message_type] += 1

    def _process_message(self, message: dict) -> None:
        self.debug(f"{self._classname} process message {message}")
        message_type = message.get("Type")
        stream_id = message.get("ID")
        event = StreamEvent.get(stream_id)

        key = message.get("Key", {})
        self._update_usage_counter(stream_id, key, message_type)

        if message_type == "Refresh":
            self._emitter.emit(event.refresh_by_id, self, message)
            if message.get("Complete", True):
                self._update_usage_counter(stream_id, key, "Complete")
                self._emitter.emit(event.complete_by_id, self, message)

        elif message_type == "Update":
            self._emitter.emit(event.update_by_id, self, message)

        elif message_type == "Status":
            self._emitter.emit(event.status_by_id, self, message)

        elif message_type == "Error":
            # Detect if error is related to Post contrib request,
            # then forward event to post_id listener
            debug_message = message.get("Debug", {}).get("Message")
            if stream_id == LOGIN_STREAM_ID and debug_message:
                try:
                    debug_dict = json.loads(debug_message)
                    post_id = debug_dict.get("PostID")
                    if post_id:
                        event = StreamEvent.get(post_id)
                except json.decoder.JSONDecodeError:
                    self.error(f"Cannot decode Debug message as JSON: {debug_message}")
            self._emitter.emit(event.error_by_id, self, message)

        elif message_type == "Ack":
            if stream_id == LOGIN_STREAM_ID:
                self.debug(f"Receive Ack on login ID {stream_id}")
                event = StreamEvent.get(message.get("AckID"))
            else:
                event = StreamEvent.get(stream_id)
            self._emitter.emit(event.ack_by_id, self, message)

        elif message_type == "Ping":
            self.send_message({"Type": "Pong"})

        else:
            raise ValueError(f"Unknown message {message}")
