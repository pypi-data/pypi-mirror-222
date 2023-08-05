import pyotp


def generate_secret():
    return pyotp.random_base32()


def verify_mfa(secret: str, code: str):
    totp = pyotp.TOTP(secret)
    return totp.verify(code, valid_window=1)
