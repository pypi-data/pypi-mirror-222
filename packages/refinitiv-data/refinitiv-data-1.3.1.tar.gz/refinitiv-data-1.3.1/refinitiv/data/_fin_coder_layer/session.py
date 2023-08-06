"""Session functions."""

from typing import Optional, TYPE_CHECKING

from .._config_functions import load_config, get_config
from .._core.session import get_default, set_default, is_open, is_closed
from .._core.session._session_definition import Definition
from .._log import root_logger


if TYPE_CHECKING:
    from .._core.session import Session


def open_session(
    name: Optional[str] = None,
    app_key: Optional[str] = None,
    config_name: Optional[str] = None,
) -> "Session":
    """
    Opens and returns a session.

    Parameters
    ----------
    name: str, optional
        Session name from the config file.
    app_key: str, optional
        The application key.
    config_name: str, optional
        The config name. If provided, overrides default config.

    Returns
    -------
    Session
    """
    # Because it's a path in configuration profile, not a session name,
    # but we can't change argument name, because it's a public API
    config_path = name
    del name

    _definition = Definition
    _load_config = load_config
    _config_object = get_config()
    _set_default = set_default
    return _open_session(**locals())


def close_session() -> None:
    """
    Closes the previously opened session.

    Returns
    -------
    None
    """
    _get_default = get_default
    _close_session(**locals())


def _open_session(**kwargs) -> "Session":
    config_name_for_err = "default"
    app_key = kwargs.pop("app_key")
    config_name = kwargs.pop("config_name")

    _definition = kwargs.pop("_definition")
    _load_config = kwargs.pop("_load_config")
    _config_object = kwargs.pop("_config_object")
    _set_default = kwargs.pop("_set_default")

    if config_name:
        _load_config(config_name)
        config_name_for_err = "config_name"

    name = kwargs.pop("config_path") or _config_object.get_param("sessions.default")

    try:
        _config_object.get_param(f"sessions.{name}")
    except Exception:
        raise NameError(
            f"Cannot open session {name}\n"
            f"This session is not defined in the {config_name_for_err} configuration file"
        )

    if app_key:
        _config_object.set_param(param=f"sessions.{name}.app-key", value=app_key)

    session = _definition(name=name).get_session()

    _set_default(session)
    session.open()

    return session


def _close_session(**kwargs) -> None:
    _get_default = kwargs.pop("_get_default")

    try:
        default_session = _get_default()
    except AttributeError:
        root_logger().info("Nо default session to close")
    else:
        if is_open(default_session):
            default_session.info("Closing session")
            default_session.close()
        if is_closed(default_session):
            default_session.info("Session is closed")
