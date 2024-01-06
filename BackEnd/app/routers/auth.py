from fastapi import APIRouter
from pydantic import BaseModel, Field



router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

class UserRequest(BaseModel):
    user_name: str = Field(min_length=1)
    hashed_password: str = Field(min_length=1)
    role: str = Field(min_length=1)
    email: str = Field(min_length=1)