from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends,HTTPException
from pydantic import BaseModel, Field
from starlette import status
from sqlalchemy.orm import Session
from app.models import Person
from app.database import SessionLocal
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


SECRET_KEY = 'MOVIEAPP'
ALGORITHM = 'HS256'


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class PersonRequest(BaseModel):
    user_name: str = Field(min_length=1)
    plain_text_password: str = Field(min_length=1)
    # role: str = Field(min_length=1)
    email: str = Field(min_length=1)

    
class Token(BaseModel):
    access_token: str
    token_type: str


# To check if person's username and password is correct
def authenticate_user(user_name: str, password: str, db):
    user = db.query(Person).filter(Person.user_name == user_name).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


# to create token
def create_access_token(user_name: str, person_id: int, role: str, expires_delta: timedelta):
    encode = {'sub': user_name, 'id': person_id, 'role': role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


# to check if the token is correct / the person is authorized
# to decode a token
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        person_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or person_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user/admin.')
        return {'username': username, 'id': person_id, 'user_role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user/admin.')


# creating user
@router.post("/sign-up_user", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user_request: PersonRequest):
    
    create_user_model = Person(
        email=create_user_request.email,
        user_name=create_user_request.user_name,
        role="user",
        hashed_password=bcrypt_context.hash(create_user_request.plain_text_password),
    )

    db.add(create_user_model)
    db.commit()


# creating admin
@router.post("/sign-up_admin", status_code=status.HTTP_201_CREATED)
async def create_admin(db: db_dependency,
                      create_admin_request: PersonRequest):
    
    create_admin_model = Person(
        email=create_admin_request.email,
        user_name=create_admin_request.user_name,
        role="admin",
        hashed_password=bcrypt_context.hash(create_admin_request.plain_text_password),
    )

    db.add(create_admin_model)
    db.commit()


# log in for user/admin
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user/admin.')
    
    token = create_access_token(user.user_name, user.id, user.role, timedelta(minutes=120))

    return {'access_token': token, 'token_type': 'bearer'}
