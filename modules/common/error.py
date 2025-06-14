class ConfigError(Exception):
    """Base error for config related issues."""
    def __init__(self, module: str, message: str):
        super().__init__(f"[{module}] {message}")
        self.module = module

class ConfigDefaultNotFoundError(ConfigError):
    """Raised when the default config file is missing."""
    pass

class ConfigNotFoundError(ConfigError):
    """Raised when the main config file is missing."""
    pass

class FirstRunWarning(Warning):
    """Warning raised on first run when config is created."""
    def __init__(self, module: str, message: str):
        super().__init__(f"[{module}] {message}")
        self.module = module
