from ormar import Text

from Services.Models.BaseModel import BaseModel


class Senator(BaseModel):
    Serial = Text(primary_key=True)
    Name = Text()
    Identification = Text()
    TypeIdentification = Text()

    class Meta:
        tablename = "Senator"
