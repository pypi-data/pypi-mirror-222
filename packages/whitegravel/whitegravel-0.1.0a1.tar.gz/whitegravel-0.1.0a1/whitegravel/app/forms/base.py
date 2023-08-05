class FormBase:
    def __init__(self) -> None:
        pass

    def dict(self):
        return {k: self.__getattribute__(k) for k in self.__annotations__}
