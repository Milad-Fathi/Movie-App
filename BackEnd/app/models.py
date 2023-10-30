from database import Base
from sqlalchemy import Column, INTEGER, String, ForeignKey


class Person(Base):
    __tablename__ = 'person'

    id = Column(INTEGER, primary_key=True, index=True)
    user_name = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)
    email = Column(String, unique=True)


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(INTEGER, primary_key=True, index=True)
    message = Column(String)
    film_id = Column(INTEGER, ForeignKey("film.id"))
    person_id = Column(INTEGER, ForeignKey("person.id"))