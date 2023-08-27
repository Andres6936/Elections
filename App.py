from fastapi import FastAPI
from peewee import DoesNotExist

from Services.Models.General.Pagination import Pagination
from Services.Models.Personal.Personal import Personal, PersonalBody
from Services.Models.Personal.PersonalCOVI import PersonalCOVI
from Services.Models.Personal.QueryBySerial import QueryBySerial

app = FastAPI()


@app.get("/")
def GetRoot():
    return {"Hello": "World"}


@app.get("/personal/count")
def CountPersonal():
    count = Personal.select('*').count()
    return {'Count': count}


@app.post("/personal/find/all")
def FindAllPersonal(pagination: Pagination):
    if pagination.Page < 1:
        return {'Body': 'The pagination is 1-index based'}
    query = Personal.select().paginate(pagination.Page, pagination.PageSize)
    return {'Items': [item.__data__ for item in query]}


@app.post("/personal/find/one")
def FindOnePersonal(query: QueryBySerial):
    try:
        personal = Personal.get(Personal.Serial == query.Serial)
        return {'Item': personal.__data__}
    except DoesNotExist:
        return {'Body': 'Not Found'}


@app.post("/personal/insert")
def InsertPersonal(personal: PersonalBody):
    personal = Personal.From(personal)
    personal.save()
    return {'Body': 'Success'}


@app.put("/personal/find/update")
def UpdatePersonal(personal: PersonalBody):
    pass


@app.delete("/personal/delete")
def RemovePersonal(query: QueryBySerial):
    pass


@app.get("/personal/covi/count")
def CountPersonalCOVI():
    count = PersonalCOVI.select('*').count()
    return {'Count': count}


if __name__ == '__main__':
    pass
