
from fastapi import APIRouter




router = APIRouter(
    prefix='/home',
    tags=['home']
)



@router.get("/")
async def hello_world():
    return{"Hello": "World"}