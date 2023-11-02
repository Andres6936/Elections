from ormar import Text

from Services.Models.BaseModel import BaseModel


class SenatorExpense(BaseModel):
    Serial = Text(primary_key=True)
    Consul = Text()
    District = Text()
    Department = Text()
    PoliticalParty = Text()
    Concept = Text()
    Name = Text()
    TypePerson = Text()
    Value = Text()
    DescriptionConcept = Text()
    TypePropaganda = Text()
    Senator = Text()

    class Meta:
        tablename = "SenatorExpense"
