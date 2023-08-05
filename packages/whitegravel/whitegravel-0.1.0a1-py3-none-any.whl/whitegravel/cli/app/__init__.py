import click


@click.group()
def app():
    pass


from .start import start
from .setup import setup

app.add_command(start)
app.add_command(setup)
