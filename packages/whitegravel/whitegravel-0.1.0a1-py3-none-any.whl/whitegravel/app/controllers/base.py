from ...db.app.functions import create_engine
from ...db.app.functions import Session


class BaseController:
    __session: Session

    def __init__(self) -> None:
        self.__session = Session(create_engine())

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.session.__exit__(*exc)

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.session.commit()
