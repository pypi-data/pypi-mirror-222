import click


@click.command("setup")
def setup():
    from ... import config

    config.loader()

    import qrcode
    from datetime import datetime

    from ..functions import subtitle
    from ..functions import title

    from whitegravel.app.security.passwords import is_strong_password
    from whitegravel.app.security.passwords import generate_password
    from whitegravel.app.security.passwords import get_password_hash
    from whitegravel.app.security.mfa import generate_secret

    from whitegravel.constants.app import PASSWORD_POLICY
    from whitegravel.constants.app import ZERO_DATETIME
    from whitegravel.constants.app import SYSTEM_USER

    from whitegravel.db.app.tables import UserTable
    from whitegravel.db.app.functions import Session
    from whitegravel.db.app.functions import create_engine

    from whitegravel.app.controllers.user import UserController

    click.clear()
    title("Welcome to whitegravel Server Setup")
    subtitle("Step 1 - System User Configuration")
    system_email: str = click.prompt(
        click.style("Please enter an email for system user", fg="green"), type=str
    )

    subtitle("Step 2 - First User Creation")

    username: str = click.prompt(
        click.style("Please enter an username", fg="green"), type=str
    )
    password: str = None

    while password is None or not is_strong_password(
        password=password, **PASSWORD_POLICY
    ):
        if password is not None:
            click.echo(
                click.style(
                    "The password is weak. Password policy requires: "
                    "lowercase, uppercase, symbols, numbers and minimun "
                    "length of 8 chars.",
                    fg="bright_red",
                    bold=True,
                )
            )

        password: str = click.prompt(
            click.style("Please enter a password", fg="green"),
            hide_input=True,
            confirmation_prompt=True,
        )

    email: str = click.prompt(
        click.style("Please enter an email", fg="green"), type=str
    )
    first_name: str = click.prompt(
        click.style("Please enter a first name", fg="green"), type=str
    )
    last_name: str = click.prompt(
        click.style("Please enter a last name", fg="green"), type=str
    )

    # Creating System User
    with Session(create_engine()) as session:
        now = datetime.now()

        system_user = UserTable(
            username=SYSTEM_USER,
            first_name="SYSTEM",
            last_name="ACCOUNT",
            email=system_email.lower(),
            created_by=SYSTEM_USER,
            updated_by=SYSTEM_USER,
            created_at=now,
            updated_at=now,
            password=get_password_hash(generate_password(128)),
            last_password_set_at=ZERO_DATETIME,
            mfa=generate_secret(),
        )

        session.merge(system_user)
        session.commit()

    with UserController() as ctrl:
        first_user = ctrl.create(
            current_username=SYSTEM_USER,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

    with Session(create_engine()) as session:
        now = datetime.now()

        first_user_entry = session.get(UserTable, username)
        first_user_entry.password = get_password_hash(password=password)
        first_user_entry.last_password_set_at = now
        first_user_entry.updated_at = now

        session.bulk_save_objects([first_user_entry])
        session.commit()

    with UserController() as ctrl:
        subtitle("Step 3 - Configure Multi-Factor Authentication")
        mfa_secret = ctrl.get_mfa(username=first_user.username, password=password)

        qr = qrcode.QRCode()
        qr.add_data(f"otpauth://totp/whitegravel%20Server?secret={mfa_secret}")
        qr.print_ascii()

        mfa_code: str = click.prompt(
            click.style(
                "Please, scan the QR Code to configure the OTP App and write the generated code to complete the configuration",
                fg="green",
            ),
            type=str,
        )

        ctrl.enable_mfa(username=first_user.username, password=password, code=mfa_code)
