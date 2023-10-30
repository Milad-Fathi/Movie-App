
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



from pydantic import BaseSettings

class Settings(BaseSettings):
    db_password: str = ""

    class Config:
        env_file = ".env"



settings = Settings()
# db_password = settings.db_password

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{settings.db_password}@localhost/MovieAppDatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
