import logging
from pathlib import Path

from modules.common.config_base import BaseConfig

logger = logging.getLogger('shittim.config')

class Config(BaseConfig):
    def __init__(self):
        super().__init__(
            module_name='shittim',
            config_dir=Path(__file__).parent,
            config_file='shittim.config.yaml',
            default_file='shittim.config.default.yaml'
        )
