from fastapi import FastAPI
import models
from database import engine
from routers import home, admin

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(home.router)
app.include_router(admin.router)
