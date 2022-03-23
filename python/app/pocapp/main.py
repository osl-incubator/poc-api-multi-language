from fastapi import FastAPI

from pocapp.routers import simple
from pocapp.routers import storage

app = FastAPI()


app.include_router(simple.router)
app.include_router(storage.router)
