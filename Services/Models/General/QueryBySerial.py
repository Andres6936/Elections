from pydantic import BaseModel


class QueryBySerial(BaseModel):
    Serial: str
