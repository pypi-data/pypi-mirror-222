import click


@click.group()
def app():
    pass


def alembic():
    from ...db.alembic.alembic import Alembic
    from ...db.app.functions import create_url

    return Alembic(create_url(), "app")


@app.add_command
@click.command("revision")
@click.option("-m", "--message", type=str, required=True)
@click.option("-a", "--auto", type=bool, is_flag=True)
def revision(message: str, auto: bool):
    alembic().create_revision(message=message, autogenerate=auto)


@app.add_command
@click.command("upgrade")
@click.option("-r", "--revision", type=str, default="head")
def upgrade(revision: str):
    alembic().upgrade_revision(revision)


@app.add_command
@click.command("downgrade")
@click.option("-r", "--revision", type=str, required=True)
def downgrade(revision: str):
    alembic().downgrade_revision(revision)


@app.add_command
@click.command("stamp")
@click.option("-r", "--revision", type=str)
@click.option("-p", "--purge", type=bool, is_flag=True)
def stamp(revision: str, purge: bool):
    alembic().stamp_revision(revision, purge=purge)


@app.add_command
@click.command("current")
def current():
    alembic().check_current()


@app.add_command
@click.command("history")
def history():
    print()
    alembic().history()
    print()
