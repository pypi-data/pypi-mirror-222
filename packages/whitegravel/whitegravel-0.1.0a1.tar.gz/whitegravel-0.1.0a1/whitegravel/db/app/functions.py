from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy import URL
from sqlalchemy.orm import Session
from sqlalchemy import Engine

from ...config import settings

engine: Engine = None


def create_url() -> URL:
    db_settings = settings.database.app

    url = URL.create(
        drivername="postgresql+psycopg2",
        username=db_settings.username,
        password=db_settings.password,
        host=db_settings.host,
        port=db_settings.port,
        database=db_settings.database,
    )

    return url


def create_engine() -> Engine:
    _globals = globals()

    if _globals["engine"]:
        return _globals["engine"]

    db_settings = settings.database.app

    url = create_url()

    _globals["engine"] = sa_create_engine(
        url=url, pool_size=db_settings.thread_connection_pool_size
    )

    return _globals["engine"]
