import requests

from .event import StreamEvent
from .stream_connection import StreamConnection, LOGIN_STREAM_ID
from .stream_cxn_state import StreamCxnState
from ..._core.session import SessionCxnType


class RDPStreamConnection(StreamConnection):
    @property
    def subprotocol(self) -> str:
        return "rdp_streaming"

    def get_login_message(self):
        message = {
            "method": "Auth",
            "streamID": f"{LOGIN_STREAM_ID:d}",
        }
        if self._session._get_session_cxn_type() == SessionCxnType.DESKTOP:
            message.update(
                {
                    "appKey": self._session.app_key,
                    "authorization": f"Bearer {self._session._access_token}",
                }
            )
        else:
            message["token"] = self._session._access_token
        return message

    def _handle_login_message(self, message: dict):
        """
        Parameters
        ----------
        message
            {
                'state': {
                    'code': 200,
                    'status': 'OK',
                    'message': 'Access token is valid'
                },
                'type': 'Ack',
                'streamID': '2'
            }
        """
        state = message.get("state", {})
        status = state.get("status")
        code = state.get("code")

        # "OK" for qps and "Ok" for tds
        if status == "OK" or status == "Ok":
            self._state = StreamCxnState.MessageProcessing
            self._connection_result_ready.set()

        elif status == "Closed" or status == "Error" or code == requests.codes.bad:
            self.debug(f"{self._classname} received a bad message: state={self.state}, message={message}")
            self._state = StreamCxnState.Disconnected
            not self.can_reconnect and self._connection_result_ready.set()
            self._config.info_not_available()
            self._listener.close()

        else:
            raise ValueError(
                f"{self._classname}._handle_login_message() | Don't know what to do "
                f"state={self.state}, message={message}"
            )

    def _process_message(self, message: dict) -> None:
        self.debug(f"{self._classname} process message {message}")
        stream_id = message.get("streamID")
        message_type = message.get("type")
        event = StreamEvent.get(stream_id)

        if message_type == "Ack":
            self._emitter.emit(event.ack_by_id, self, message)

        elif message_type == "Response":
            self._emitter.emit(event.response_by_id, self, message)

        elif message_type == "Update":
            self._emitter.emit(event.update_by_id, self, message)

        elif message_type == "Alarm":
            self._emitter.emit(event.alarm_by_id, self, message)

        elif message_type == "Error":
            self._emitter.emit(event.error_by_id, self, message)

        elif message_type == "Heartbeat":
            # do nothing
            pass

        else:
            raise ValueError(f"Unknown message {message}")
