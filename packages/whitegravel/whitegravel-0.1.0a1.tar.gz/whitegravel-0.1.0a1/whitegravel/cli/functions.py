import click


def title(title: str):
    title_len = len(title)
    dec = "#"
    dec_len = 12

    padding = " " * (dec_len - 1)

    header = (dec * dec_len) + ("#" * title_len) + (dec * dec_len)
    footer = header

    click.echo(click.style(header, fg="yellow"))

    click.echo(click.style(dec + padding + title + padding + dec, fg="yellow"))

    click.echo(click.style(footer + "\n", fg="yellow"))


def subtitle(subtitle: str):
    click.echo(click.style(f"\n{subtitle}\n{'-' * len(subtitle)}", bold=True))
