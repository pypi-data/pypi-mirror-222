import os
from typing import Optional

from ._external_libraries import python_configuration as ext_config_mod  # noqa
from ._configure import get_config as _get_config, _read_config_file, _RDPConfig

RDConfig = _RDPConfig


def get_config() -> RDConfig:
    """
    Returns
    -------
    config object
    """
    return _get_config()


def load_config(path: Optional[str]) -> RDConfig:
    """
    Load user's config file and set this file as default.

    Parameters
    ----------
        path: str
            Path to user's config file.

    Raises
    ----------
    Exception
        If can't find file by path that user provided

    Returns
    ----------
    config object
    """
    return _load_config_and_set_default(path)


def _load_config_and_set_default(path: Optional[str]) -> _RDPConfig:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Can't find file: {path}. Current working folder {os.getcwd()}")

    loaded_config = _read_config_file(path)
    user_config = ext_config_mod.config_from_dict(loaded_config)

    config = _get_config()
    config._set_config_index(0, user_config)
    return config
