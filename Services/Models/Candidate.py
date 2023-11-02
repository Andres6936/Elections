from ormar import Text

from Services.Models.BaseModel import BaseModel


class CandidateBody(BaseModel):
    Candidate: str
    PoliticalParty: str


class Candidate(BaseModel):
    Serial: str = Text(primary_key=True, max_length=255)
    Candidate: str = Text()
    PoliticalParty: str = Text()

    class Meta:
        tablename = "Candidate"
