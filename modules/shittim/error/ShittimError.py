from modules.common.error import ConfigError, ConfigDefaultNotFoundError

class ShittimError(ConfigError):
    def __init__(self, message: str):
        super().__init__('shittim', message)

class ShittimConfigDefaultNotFoundError(ConfigDefaultNotFoundError):
    def __init__(self, message: str):
        super().__init__('shittim', message)
