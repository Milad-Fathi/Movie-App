
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from database import SessionLocal
from models import Film


router = APIRouter(
    prefix='/home',
    tags=['home']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
# user_dependency = Annotated[dict, Depends(get_current_user)]



# class FilmRequest(BaseModel):
#     title: str = Field(min_length=1)
#     description: str = Field(min_length=5, max_length=250)
#     rating: int = Field(gt=0, lt=6)
#     cover: str = Field(min_length=1)
#     movie_play_link: str = Field(min_length=1)
#     date: str = Field(min_length=1)
#     budget: int = Field(gt=0)
#     language:str = Field(min_length=1)
#     duration: int = Field(gt=0)





@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Film).limit(2).all()
