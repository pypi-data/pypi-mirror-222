from datetime import datetime

SERVER_NAME = "whitegravel Server"
SYSTEM_USER = "system"
TOKEN_TYPE_USER = "TOKEN_TYPE_USER"
TOKEN_TYPE_API = "TOKEN_TYPE_API"
ZERO_DATETIME = datetime.fromtimestamp(0.0)
MAX_VALUE_BIGINT = 9223372036854776
MAX_VALUE_PAGE = 999999

PASSWORD_POLICY = dict(
    require_lowercase=True,
    require_numbers=True,
    require_symbols=True,
    require_uppercase=True,
    minimum_lenght=8,
)

RESERVED_USERNAMES = (SYSTEM_USER, "anonymous", "anon")
