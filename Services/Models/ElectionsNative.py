from ormar import Text

from Services.Models.BaseModel import BaseModel


class ElectionsNative(BaseModel):
    Serial = Text(primary_key=True)
    Department = Text()
    Municipality = Text()
    Stand = Text()
    VotingTable = Text()
    Votes = Text()
    Candidate = Text()

    class Meta:
        tablename = "ElectionsNative"
