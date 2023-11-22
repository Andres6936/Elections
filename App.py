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

app.include_router(OrmarCRUDRouter(schema=Candidate, paginate=99))
app.include_router(OrmarCRUDRouter(schema=ElectionsNational, paginate=99))
app.include_router(OrmarCRUDRouter(schema=ElectionsNative, paginate=99))
app.include_router(OrmarCRUDRouter(schema=IncomeBase, paginate=99))
app.include_router(OrmarCRUDRouter(schema=Items, paginate=99))
app.include_router(OrmarCRUDRouter(schema=Senator, paginate=99))
app.include_router(OrmarCRUDRouter(schema=SenatorExpense, paginate=99))

if __name__ == '__main__':
    uvicorn.run("App:app", port=8000, log_level="info")
