from ormar import Text

from Services.Models.BaseModel import BaseModel


class Senator(BaseModel):
    Serial: str = Text(primary_key=True)
    Name: str = Text()
    Identification: str = Text()
    TypeIdentification: str = Text()

    class Meta:
        tablename = "Senator"
