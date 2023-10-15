import uvicorn
from fastapi import FastAPI
from peewee import DoesNotExist

from Services.Models.Elecciones.Candidates import Candidates, CandidateBody
from Services.Models.General.Pagination import Pagination
from Services.Models.General.QueryBySerial import QueryBySerial

app = FastAPI()


@app.get("/")
def GetRoot():
    return {"Hello": "World"}


@app.get("/candidates/count")
def CountPersonal():
    count = Candidates.select('*').count()
    return {'Count': count}


@app.post("/candidates/find/all")
def FindAllPersonal(pagination: Pagination):
    if pagination.Page < 1:
        return {'Body': 'The pagination is 1-index based'}
    query = Candidates.select().paginate(pagination.Page, pagination.PageSize)
    return {'Items': [item.__data__ for item in query]}


@app.post("/candidates/find/one")
def FindOnePersonal(query: QueryBySerial):
    try:
        personal = Candidates.get(Candidates.Serial == query.Serial)
        return {'Item': personal.__data__}
    except DoesNotExist:
        return {'Body': 'Not Found'}


@app.post("/candidates/insert")
def InsertPersonal(personal: CandidateBody):
    personal = Candidates.From(personal)
    personal.save()
    return {'Body': 'Success'}


@app.put("/candidates/update")
def UpdatePersonal(personal: CandidateBody):
    try:
        item = Candidates.get(Candidates.Serial == personal.Serial)
        item.Candidate = personal.Candidate
        item.PoliticalParty = personal.PoliticalParty

        item.save()
        return {'Item': item.__data__}
    except DoesNotExist:
        return {'Body': 'Not Found'}


@app.delete("/candidates/delete")
def RemovePersonal(query: QueryBySerial):
    try:
        personal = Candidates.get(Candidates.Serial == query.Serial)
        personal.delete_instance()
        return {'Body': 'Success'}
    except DoesNotExist:
        return {'Body': 'Not Found'}


if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, log_level="info")
