from fastapi import FastAPI
import models
from database import engine
from routers import home

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def hello_world():
    return{"Hello": "World"}