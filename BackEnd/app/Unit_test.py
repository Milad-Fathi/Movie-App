from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)



# testing post method ( add_movie )
def test_add_film_admin():
    response = client.post("/admin/addFilm",json={
        "title": "film5",
        "description": "string",
        "rating": 1,
        "cover": "cover5",
        "movie_play_link": "link5",
        "date": "string",
        "budget": 1,
        "language": "string",
        "duration": 1
    })
    assert response.status_code == 201



# testing get method (read_movie by its title)
def test_read_film_admin():
    response = client.get("/admin/readFilm/?film_title=f2")
    assert response.status_code == 200
    assert response.json() == {"title":"f2","description":"string","cover":"string2","movie_play_link":"string2","budget":2,"duration":2,"rating":2,"id":4,"date":"string","language":"string"}



# testing put method (update_movie)
def test_update_film_admin():
    response = client.put("/admin/updateFilm/?film_title=f3",json={
        "title": "f3",
        "description": "string",
        "rating": 3,
        "cover": "string3",
        "movie_play_link": "string3",
        "date": "string",
        "budget": 3,
        "language": "string",
        "duration": 3
    })
    assert response.status_code == 204



# testing delete method (delete_movie)
def test_delete_film_admin():
    response = client.delete("/admin/deleteFilm/?film_title=film1")

    assert response.status_code == 204


