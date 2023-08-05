from pathlib import Path
from dynaconf import Dynaconf
from dynaconf import Validator

from .loader import loader
from .model import Settings

settings: Settings | Dynaconf = None


def load_file_config(settings_folder: Path | str):
    if isinstance(settings_folder, str):
        settings_folder = Path(settings_folder)

    glob = globals()

    glob["settings"] = Dynaconf(
        envvar_prefix="whitegravel_SERVER",
        env_switcher="whitegravel_SERVER_MODE",
        settings_files=[
            str(p.absolute()) for p in settings_folder.iterdir() if p.is_file()
        ],
        merge_enabled=True,
    )


def load_vault_config(vault_url: str, token: str):
    glob = globals()

    glob["settings"] = Dynaconf(
        environment=True,
        vault_enabled=True,
        vault={"url": vault_url, "token": token},
        merge_enabled=True,
        # validators=[
        #     # Ensure some parameters exist (are required)
        #     Validator('VERSION', 'AGE', 'NAME', must_exist=True),
        #     # Ensure some password cannot exist
        #     Validator('PASSWORD', must_exist=False),
        #     # Ensure some parameter meets a condition
        #     # conditions: (eq, ne, lt, gt, lte, gte, identity, is_type_of, is_in, is_not_in)
        #     Validator('AGE', lte=30, gte=10),
        #     # validate a value is eq in specific env
        #     Validator('PROJECT', eq='hello_world', env='production'),
        #     # Ensure some parameter (string) meets a condition
        #     # conditions: (len_eq, len_ne, len_min, len_max, cont)
        #     # Determines the minimum and maximum length for the value
        #     Validator("NAME", len_min=3, len_max=125),
        #     # Signifies the presence of the value in a set, text or word
        #     Validator("DEV_SERVERS", cont='localhost'),
        #     # Checks whether the length is the same as defined.
        #     Validator("PORT", len_eq=4),
        #     # Ensure java_bin is returned as a Path instance
        #     Validator("JAVA_BIN", must_exist=True, cast=Path),
        #     # Ensure a value meets a condition specified by a callable
        #     Validator("VERSION", must_exist=True, condition=lambda v: v.startswith("1.")),
        # ]
    )


# `envvar_prefix` = export envvars with `export whitegravel_FOO=bar`.
# `settings_files` = Load these files in the order.
