
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from app.database import SessionLocal
from app.models import Film, Genre

# from database import SessionLocal
# from models import Film


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




# return top 5 film of the list 
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Film).limit(5).all()



# return specific movie ,search by its title
@router.get("/search/", status_code=status.HTTP_200_OK)
async def search_movie(db: db_dependency,
                    film_title: str):
    film_model = db.query(Film).filter(Film.title == film_title).first()
    if film_model is not None:
        return film_model
    raise HTTPException(status_code=404, detail="film not found")


# ***********************************************
# not tested
# ***********************************************
# return all genres
@router.get("/genre", status_code=status.HTTP_200_OK)
async def read_genre(db: db_dependency, name_genre):
    genre_model = db.query(Genre).filter(Genre.name == name_genre)
    if genre_model is not None:
        return genre_model
    raise HTTPException(status_code=404, detail="genre not found")

# ***********************************************
# not tested
# ***********************************************











## return movies in specific genre
# @router.get("/genre/", status_code=status.HTTP_200_OK)
# async def read_by_genre(db: db_dependency, film_genre: str):
    

