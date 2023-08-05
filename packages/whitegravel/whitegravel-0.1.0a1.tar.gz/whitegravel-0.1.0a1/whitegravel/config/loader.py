def loader():
    import os

    from whitegravel import config
    from whitegravel.exceptions.config import ConfigError

    vault_url = os.getenv("VAULT_URL")
    vault_token = os.getenv("VAULT_TOKEN")
    config_folder = os.getenv("CONFIG_FOLDER")

    if not ((vault_token and vault_url) or config_folder):
        raise ConfigError(
            "Required environment variables doesn't setted: "
            "'VAULT_URL' and 'VAULT_TOKEN' to retrieve config "
            "from vault or 'CONFIG_FOLDER' to retrieve from files"
        )

    if vault_token and vault_url:
        config.load_vault_config(vault_url=vault_url, token=vault_token)

    else:
        config.load_file_config(settings_folder=config_folder)
