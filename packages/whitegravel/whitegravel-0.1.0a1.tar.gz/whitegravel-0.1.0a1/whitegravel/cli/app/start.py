import click


@click.command("start")
@click.option("-w", "--workers", type=click.IntRange(min=3), default=None)
@click.option("-b", "--bind", type=str, default="127.0.0.1")
@click.option("-p", "--port", type=click.IntRange(min=1, max=65535), default=8000)
def start(workers: int, bind: str, port: int):
    from ... import config

    config.loader()

    import uvicorn

    uvicorn.run(
        app="whitegravel.app.app:app",
        host=bind,
        port=port,
        workers=workers,
        root_path=config.settings.app.get("root_path", ""),
    )
