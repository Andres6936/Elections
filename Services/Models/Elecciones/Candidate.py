import shortuuid
from peewee import TextField
from pydantic import BaseModel

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class CandidateBody(BaseModel):
    Candidate: str
    PoliticalParty: str


class Candidate(EleccionesBase):
    Serial = TextField(primary_key=True)
    Candidate = TextField()
    PoliticalParty = TextField()

    @staticmethod
    def From(body: CandidateBody):
        return Candidate.create(
            Serial=shortuuid.ShortUUID().random(length=6),
            Candidate=body.Candidate,
            PoliticalParty=body.PoliticalParty,
        )
