import uvicorn
from fastapi import FastAPI
from fastapi_crudrouter import OrmarCRUDRouter

from Services.Models.Candidate import Candidate
from Services.Models.ElectionsNational import ElectionsNational
from Services.Models.ElectionsNative import ElectionsNative
from Services.Models.IncomeBase import IncomeBase
from Services.Models.Items import Items
from Services.Models.Senator import Senator
from Services.Models.SenatorExpense import SenatorExpense

app = FastAPI()

app.include_router(OrmarCRUDRouter(schema=Candidate))
app.include_router(OrmarCRUDRouter(schema=ElectionsNational))
app.include_router(OrmarCRUDRouter(schema=ElectionsNative))
app.include_router(OrmarCRUDRouter(schema=IncomeBase))
app.include_router(OrmarCRUDRouter(schema=Items))
app.include_router(OrmarCRUDRouter(schema=Senator))
app.include_router(OrmarCRUDRouter(schema=SenatorExpense))

if __name__ == '__main__':
    uvicorn.run("App:app", port=8000, log_level="info")
