from ormar import Text

from Services.Models.BaseModel import BaseModel


class Items(BaseModel):
    Serial: str = Text(primary_key=True)
    Line: str = Text()
    Item: str = Text()
    Price: str = Text()
    Amount: str = Text()
    UoM: str = Text()
    Total: str = Text()
    CDP: str = Text()

    class Meta:
        tablename = "Items"
