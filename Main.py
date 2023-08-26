from fastapi import FastAPI

from Services.Models.Personal.Personal import Personal
from Services.Models.Personal.PersonalCOVI import PersonalCOVI

app = FastAPI()


@app.get("/")
def GetRoot():
    return {"Hello": "World"}


@app.get("/personal/count")
def CountPersonal():
    count = Personal.select('*').count()
    return {'Count': count}


@app.post("/personal/find/all")
def FindAllPersonal():
    pass


@app.post("/personal/find/one")
def FindOnePersonal():
    pass


@app.post("/personal/insert")
def InsertPersonal():
    pass


@app.put("/personal/find/update")
def UpdatePersonal():
    pass


@app.delete("/personal/delete")
def RemovePersonal():
    pass


@app.get("/personal/covi/count")
def CountPersonalCOVI():
    count = PersonalCOVI.select('*').count()
    return {'Count': count}


if __name__ == '__main__':
    pass
