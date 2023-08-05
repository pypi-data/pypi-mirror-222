import click


@click.group()
def cli():
    pass


from .app import app
from .db import db

cli.add_command(app)
cli.add_command(db)
