from fastapi import FastAPI
from ..constants.metadata import VERSION
from ..constants.app import SERVER_NAME

#! -- Configuration loading ------------------------------
from .. import config

config.loader()
#! -------------------------------------------------------

app = FastAPI(
    root_path=config.settings.app.get("root_path", ""),
    root_path_in_servers=True,
    version=VERSION,
    title=config.settings.app.get("name", SERVER_NAME),
)

#! -- Routers importing ----------------------------------
from .routes.auth import auth_router
from .routes.users import users_router

app.include_router(auth_router)
app.include_router(users_router)
#! -------------------------------------------------------
