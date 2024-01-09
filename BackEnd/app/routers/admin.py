

from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from app.database import SessionLocal
from app.models import Film, Genre, Person
from app.routers.auth import get_current_user

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
user_dependency = Annotated[dict, Depends(get_current_user)]



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
    

class GenreRequest(BaseModel):
    name : str = Field(min_length=1)



# API to create movie and add it to the database
@router.post("/addFilm", status_code=status.HTTP_201_CREATED)
async def add_movie(admin: user_dependency,
                    db:db_dependency, 
                    film_request:FilmRequest):
    
    if (admin is None) or (admin.get('user_role') != "admin"):
        raise HTTPException(status_code=401,detail='Authentication Failed')
    elif admin.get('user_role') == "admin":
        film_model = Film(**film_request.model_dump())
        db.add(film_model)
        db.commit()



#API to read movie by its "film_id" 
@router.get("/readFilm/{film_id}", status_code=status.HTTP_200_OK)
async def read_movie(admin: user_dependency,
                    db: db_dependency,
                    film_id: int = Path(gt=0)):
    
    if (admin is None) or (admin.get('user_role') != "admin"):
        raise HTTPException(status_code=401,detail='Authentication Failed')
    elif admin.get('user_role') == "admin":
        film_model = db.query(Film).filter(Film.id == film_id).first()
        if film_model is not None:
            return film_model
        raise HTTPException(status_code=404, detail="film not found")





# ********** this API is available in URL:"home/search" too,should use one of them******************************
#API to read movie by its "film_title"
@router.get("/readFilm/", status_code=status.HTTP_200_OK)
async def read_movie(db: db_dependency,
                    film_title: str):
    film_model = db.query(Film).filter(Film.title == film_title).first()
    if film_model is not None:
        return film_model
    raise HTTPException(status_code=404, detail="film not found")


#API to update movie by its "title"  
@router.put("/updateFilm/", status_code=status.HTTP_204_NO_CONTENT)
async def update_movie(admin: user_dependency,
                       db: db_dependency,
                       film_request: FilmRequest,
                       film_title: str):
    
    if (admin is None) or (admin.get('user_role') != "admin"):
        raise HTTPException(status_code=401,detail='Authentication Failed')
    elif admin.get('user_role') == "admin":

        film_model = db.query(Film).filter(Film.title == film_title).first()

        if film_model is None:
            raise HTTPException(status_code=404, detail="film not found")
        
        film_model.budget = film_request.budget
        film_model.cover = film_request.cover
        film_model.date = film_request.date
        film_model.description = film_request.description
        film_model.duration = film_request.duration
        film_model.language = film_request.language
        film_model.movie_play_link = film_request.movie_play_link
        film_model.rating = film_request.rating
        film_model.title = film_request.title

        db.add(film_model)
        db.commit()
        

#API to delete movie by its "title" 
@router.delete("/deleteFilm/",status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(admin: user_dependency,
                       db: db_dependency,
                       film_title: str):
    
    if (admin is None) or (admin.get('user_role') != "admin"):
        raise HTTPException(status_code=401,detail='Authentication Failed')
    elif admin.get('user_role') == "admin":
        
        film_model = db.query(Film).filter(Film.title == film_title).first()

        if film_model is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        db.query(Film).filter(Film.title == film_title).delete()

        db.commit()



# add genre
@router.post("/addGenre", status_code=status.HTTP_201_CREATED)
async def add_genre(db: db_dependency,
                    genre_request: GenreRequest):
    genre_model = Genre(**genre_request.model_dump())
    db.add(genre_model)
    db.commit()

    


# read all users
@router.get("/readAllUsers", status_code=status.HTTP_200_OK)
async def read_all( admin: user_dependency, 
                    db: db_dependency):
    
    if (admin is None) or (admin.get('user_role') != "admin"):
        raise HTTPException(status_code=401,detail='Authentication Failed')
    elif admin.get('user_role') == "admin":
        return db.query(Person).all()


# delete user
@router.delete("/deleteUser/",status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(admin: user_dependency,
                       db: db_dependency,
                       user_name: str):
    
    if (admin is None) or (admin.get('user_role') != "admin"):
        raise HTTPException(status_code=401,detail='Authentication Failed')
    elif admin.get('user_role') == "admin":
        
        user_model = db.query(Person).filter(Person.user_name == user_name).first()

        if user_model is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        db.query(Person).filter(Person.user_name == user_name).delete()

        db.commit()



# read admin
    


# updating user



# updating admin




# maybe not needed *******************************************
    
# deleting user
    

# deleting admin