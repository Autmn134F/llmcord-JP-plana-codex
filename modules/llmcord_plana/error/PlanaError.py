from modules.common.error import (
    ConfigError,
    ConfigDefaultNotFoundError,
    FirstRunWarning,
)


class PlanaError(ConfigError):
    """PLANA系共通の基底例外"""
    def __init__(self, message: str):
        super().__init__('llmcord_plana', message)


class PlanaConfigNotFoundError(PlanaError):
    HOW_TO_FIX = (
        "[HOW TO FIX]: 通常は起動時に自動的に設定ファイルが生成されます。",
        "基底コンフィグファイルが欠如している可能性があります。",
    )

    def __init__(self, message: str):
        super().__init__(f"{message}\n {self.HOW_TO_FIX}")


class PlanaDefaultConfigNotFound(ConfigDefaultNotFoundError):
    HOW_TO_FIX = (
        "[HOW TO FIX]: 基底コンフィグファイルが欠如しています。再インストールするか、リポジトリから取得してください。",
    )

    def __init__(self, message: str):
        super().__init__('llmcord_plana', f"{message}\n {self.HOW_TO_FIX}")


class PlanaFirstRunWarning(FirstRunWarning):
    def __init__(self, message: str):
        super().__init__('llmcord_plana', message)
