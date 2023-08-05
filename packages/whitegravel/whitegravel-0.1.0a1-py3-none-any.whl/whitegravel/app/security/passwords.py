import re
import secrets

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["ldap_salted_sha512"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def is_older_password(password: str, history: list[bytes]) -> bool:
    for entry in history:
        if verify_password(password=password, salted_password=entry):
            return True

    return False


def is_strong_password(
    password: str,
    require_symbols: bool = False,
    require_uppercase: bool = False,
    require_lowercase: bool = False,
    require_numbers: bool = False,
    minimum_lenght: int = 0,
    maximum_lenght: int = 256,
):
    policy = ""

    if require_symbols:
        policy += "(?=.*[^a-zA-Z0-9])"

    if require_uppercase:
        policy += "(?=.*[A-Z])"

    if require_lowercase:
        policy += "(?=.*[a-z])"

    if require_numbers:
        policy += "(?=.*[0-9])"

    policy += ".{%s,%s}" % (minimum_lenght, maximum_lenght)

    policyx = re.compile(policy, re.MULTILINE)

    return bool(policyx.match(password))


def get_safe_code():
    NUMLIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    code = []
    for i in range(8):
        code.append(secrets.choice(NUMLIST))

    return f"{''.join(code[4:])}-{''.join(code[:4])}"


def generate_password(length: int = 16):
    UPPERLIST = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    LOWERLIST = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    NUMLIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    SYMLIST = [
        "+",
        "?",
        "!",
        "*",
        ".",
        ",",
        " ",
        "-",
        "_",
        "^",
        "=",
        "&",
        "$",
        "@",
        "#",
        "|",
        "\\",
        "/",
        ":",
        ";",
        "<",
        ">",
    ]

    minimum = [
        secrets.choice(UPPERLIST),
        secrets.choice(LOWERLIST),
        secrets.choice(SYMLIST),
        secrets.choice(NUMLIST),
    ]

    others = []

    while len(others) + len(minimum) < length:
        others.append(
            secrets.choice(secrets.choice([UPPERLIST, LOWERLIST, SYMLIST, NUMLIST]))
        )

    def shuffle(__list: list):
        list_len = len(__list)
        choice_index = list(range(list_len))

        shuffled = []
        while len(choice_index) > 0:
            chosen = secrets.choice(choice_index)
            choice_index.pop(choice_index.index(chosen))
            shuffled.append(__list[chosen])

        return shuffled

    return "".join(shuffle(minimum + others))
