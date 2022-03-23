from fastapi import FastAPI

from pocapp.routers import simple

app = FastAPI()


app.include_router(simple.router)
