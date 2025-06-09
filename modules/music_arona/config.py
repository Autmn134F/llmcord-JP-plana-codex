import logging
from pathlib import Path

from modules.common.config_base import BaseConfig

logger = logging.getLogger('arona.config')

class Config(BaseConfig):
    def __init__(self):
        super().__init__(
            module_name='music_arona',
            config_dir=Path(__file__).parent.parent.parent,
            config_file='arona.config.yaml',
            default_file='arona.config.default.yaml'
        )

config = Config()
get = config.get
get_message = config.get_message
