from typing import Annotated
from fastapi import APIRouter, Depends,HTTPException
from pydantic import BaseModel, Field
from starlette import status
from sqlalchemy.orm import Session
from app.models import Person
from app.database import SessionLocal
from passlib.context import CryptContext

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class UserRequest(BaseModel):
    user_name: str = Field(min_length=1)
    plain_text_password: str = Field(min_length=1)
    # role: str = Field(min_length=1)
    email: str = Field(min_length=1)
    



# creating user
@router.post("/sign-in", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user_request: UserRequest):
    
    create_user_model = Person(
        email=create_user_request.email,
        user_name=create_user_request.user_name,
        role="user",
        hashed_password=bcrypt_context.hash(create_user_request.plain_text_password),
    )

    db.add(create_user_model)
    db.commit()


# creating admin
    


# read user
@router.get("/log-in/", status_code=status.HTTP_200_OK)
async def read_user(db: db_dependency,
                    user_name: str):
    user_model = db.query(Person).filter(Person.user_name == user_name).first()
    if user_model is not None:
        return user_model
    raise HTTPException(status_code=404, detail="user not found")


# read admin
    


# updating user



# updating admin




# maybe not needed *******************************************
    
# deleting user
    

# deleting admin