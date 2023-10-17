import uvicorn
from fastapi import FastAPI
from peewee import DoesNotExist

from Services.Generator.PeeweeCRUDRouter import PeeweeCRUDRouter
from Services.Models.Elecciones.Candidate import Candidate, CandidateBody
from Services.Models.Elecciones.Senator import Senator
from Services.Models.General.Pagination import Pagination
from Services.Models.General.QueryBySerial import QueryBySerial

app = FastAPI()


@app.get("/")
def GetRoot():
    return {"Hello": "World"}


@app.get("/candidate/count")
def CountPersonal():
    count = Candidate.select('*').count()
    return {'Count': count}


@app.post("/candidate/find/all")
def FindAllPersonal(pagination: Pagination):
    if pagination.Page < 1:
        return {'Body': 'The pagination is 1-index based'}
    query = Candidate.select().paginate(pagination.Page, pagination.PageSize)
    return {'Items': [item.__data__ for item in query]}


@app.post("/candidate/find/one")
def FindOnePersonal(query: QueryBySerial):
    try:
        personal = Candidate.get(Candidate.Serial == query.Serial)
        return {'Item': personal.__data__}
    except DoesNotExist:
        return {'Body': 'Not Found'}


@app.post("/candidate/insert")
def InsertPersonal(personal: CandidateBody):
    personal = Candidate.From(personal)
    personal.save()
    return {'Body': 'Success'}


@app.put("/candidate/update")
def UpdatePersonal(personal: CandidateBody):
    try:
        item = Candidate.get(Candidate.Serial == personal.Serial)
        item.Candidate = personal.Candidate
        item.PoliticalParty = personal.PoliticalParty

        item.save()
        return {'Item': item.__data__}
    except DoesNotExist:
        return {'Body': 'Not Found'}


@app.delete("/candidate/delete")
def RemovePersonal(query: QueryBySerial):
    try:
        personal = Candidate.get(Candidate.Serial == query.Serial)
        personal.delete_instance()
        return {'Body': 'Success'}
    except DoesNotExist:
        return {'Body': 'Not Found'}


app.include_router(PeeweeCRUDRouter(Senator))


if __name__ == '__main__':
    uvicorn.run("App:app", port=8000, log_level="info")
