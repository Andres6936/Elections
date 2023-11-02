from ormar import Text

from Services.Models.BaseModel import BaseModel


class Candidate(BaseModel):
    Serial: str = Text(primary_key=True)
    Candidate: str = Text()
    PoliticalParty: str = Text()

    class Meta:
        tablename = "Candidate"
