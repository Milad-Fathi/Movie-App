

from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from app.database import SessionLocal
from app.models import Film


# from database import SessionLocal
# from models import Film

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
# user_dependency = Annotated[dict, Depends(get_current_user)]



class FilmRequest(BaseModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=5, max_length=250)
    rating: int = Field(gt=0, lt=6)
    cover: str = Field(min_length=1)
    movie_play_link: str = Field(min_length=1)
    date: str = Field(min_length=1)
    budget: int = Field(gt=0)
    language:str = Field(min_length=1)
    duration: int = Field(gt=0)
    

# API to add movie to the database
@router.post("/addFilm", status_code=status.HTTP_201_CREATED)
async def add_movie(db:db_dependency, 
                    film_request:FilmRequest):
    film_model = Film(**film_request.model_dump())
    db.add(film_model)
    db.commit()


#API to read movie by its "film_id" 
@router.get("/readFilm/{film_id}", status_code=status.HTTP_200_OK)
async def readMovie(db: db_dependency,
                    film_id: int = Path(gt=0)):
    film_model = db.query(Film).filter(Film.id == film_id).first()
    if film_model is not None:
        return film_model
    raise HTTPException(status_code=404, detail="film not found")
