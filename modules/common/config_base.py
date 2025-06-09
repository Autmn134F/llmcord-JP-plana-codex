import logging
import shutil
from pathlib import Path
from typing import Any, Dict
import yaml

from modules.common.error import ConfigDefaultNotFoundError, FirstRunWarning

logger = logging.getLogger(__name__)

class BaseConfig:
    _instances: Dict[type, "BaseConfig"] = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(BaseConfig, cls).__new__(cls)
            cls._instances[cls] = instance
            instance._initialized = False
        return cls._instances[cls]

    def __init__(self, module_name: str, config_dir: Path, config_file: str, default_file: str):
        if self._initialized:
            return
        self._initialized = True

        self.module_name = module_name
        self.config_dir = config_dir
        self.config_path = config_dir / config_file
        self.default_config_path = config_dir / default_file
        self._config: Dict[str, Any] = {}

        self._ensure_config_exists()
        self._load_config()

    def _ensure_config_exists(self) -> None:
        if not self.config_path.exists():
            if not self.default_config_path.exists():
                logger.error(f"{self.config_path.name} not found. Please download it from the repository.")
                raise ConfigDefaultNotFoundError(self.module_name, f"{self.default_config_path.name} not found")
            shutil.copy(self.default_config_path, self.config_path)
            logger.info(f"Created config file at {self.config_path}. Please edit it with your settings and restart the bot.")
            raise FirstRunWarning(self.module_name, f"{self.config_path.name} not found")

    def _load_config(self) -> None:
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self._config = yaml.safe_load(f) or {}
        except Exception as e:
            logger.error(f"Error loading config file: {e}")
            self._config = {}

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self._config
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default

    def get_message(self, key: str, **kwargs) -> str:
        message = self.get(f"messages.{key}", key)
        try:
            return message.format(**kwargs)
        except (KeyError, AttributeError):
            return message
