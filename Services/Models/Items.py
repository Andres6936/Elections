from ormar import Text

from Services.Models.BaseModel import BaseModel


class Items(BaseModel):
    Serial = Text()
    Line = Text()
    Item = Text()
    Price = Text()
    Amount = Text()
    UoM = Text()
    Total = Text()
    CDP = Text()

    class Meta:
        tablename = "Items"
