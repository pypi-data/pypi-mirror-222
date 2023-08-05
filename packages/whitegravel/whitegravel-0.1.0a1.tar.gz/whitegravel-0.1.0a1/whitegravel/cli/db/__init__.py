import click


@click.group()
def db():
    pass


from .app import app

db.add_command(app)
