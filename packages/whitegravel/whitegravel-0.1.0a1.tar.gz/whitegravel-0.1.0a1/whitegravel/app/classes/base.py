from pydantic import BaseModel


class BaseClass(BaseModel):
    def export(self):
        return self.dict()


class BasicResponse(BaseClass):
    detail: str
