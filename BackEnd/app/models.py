from app.database import Base

# from database import Base


from sqlalchemy import Column, INTEGER, String, ForeignKey


class Person(Base):
    __tablename__ = 'person'

    id = Column(INTEGER, primary_key=True, index=True)
    user_name = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)
    email = Column(String, unique=True)


class PersonCommentFilm(Base):
    __tablename__ = 'personCommentFilm'

    pesron_id = Column(INTEGER, ForeignKey("person.id"), primary_key=True)
    comment_id = Column(INTEGER, ForeignKey("comment.id"), primary_key=True)
    film_id = Column(INTEGER, ForeignKey("film.id"), primary_key=True)


class PersonLiked(Base):
    __tablename__ = 'personLiked'

    person_id = Column(INTEGER, ForeignKey("person.id"), primary_key=True)
    film_id = Column(INTEGER, ForeignKey("film.id"), primary_key=True)


class PersonDisliked(Base):
    __tablename__ = 'personDisliked'

    person_id = Column(INTEGER, ForeignKey("person.id"), primary_key=True)
    film_id = Column(INTEGER, ForeignKey("film.id"), primary_key=True)

class PersonSaved(Base):
    __tablename__ = 'personSaved'

    person_id = Column(INTEGER, ForeignKey("person.id"), primary_key=True)
    film_id = Column(INTEGER, ForeignKey("film.id"), primary_key=True)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(INTEGER, primary_key=True, index=True)
    message = Column(String)


class Reply(Base):
    __tablename__ = 'reply'

    parent_id = Column(INTEGER, ForeignKey("comment.id"), primary_key=True)
    child_id = Column(INTEGER, ForeignKey("comment.id"), primary_key=True)


class Film(Base):
    __tablename__ = 'film'

    id = Column(INTEGER, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(String)
    rating = Column(INTEGER)
    cover = Column(String, unique=True)
    movie_play_link = Column(String, unique=True)
    date = Column(String)
    budget = Column(INTEGER)
    language = Column(String)
    duration = Column(INTEGER)


class FilmLinks(Base):
    __tablename__ = 'filmLinks'

    film_id = Column(INTEGER, ForeignKey("film.id"), primary_key=True)
    link_id = Column(INTEGER, ForeignKey("links.id"), primary_key=True)


class FilmGenre(Base):
    __tablename__ = 'filmGenre'

    genre_id = Column(INTEGER, ForeignKey("genre.id"), primary_key=True)
    film_id = Column(INTEGER, ForeignKey("film.id"), primary_key=True)


class Links(Base):
    __tablename__ = 'links'

    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    link = Column(String, unique=True)


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)


class Message(Base):
    __tablename__ = 'message'

    id = Column(INTEGER, primary_key=True, index=True)
    date = Column(String)
    text = Column(String)


class PersonMessage(Base):
    __tablename__ = 'personMessage'

    message_id = Column(INTEGER, ForeignKey("message.id"), primary_key=True)
    sender_id = Column(INTEGER, ForeignKey("person.id"), primary_key=True)
    receiver_id = Column(INTEGER, ForeignKey("person.id"), primary_key=True)
