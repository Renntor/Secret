from fastapi.testclient import TestClient
from main import app


test_app = TestClient(app)


def test_post_secret():
    response = test_app.post('/generate', json={'secret': "Test data?", "password": "qwerty"})
    assert response.status_code == 200


def test_get_secret():
    key = test_app.post('/generate', json={'secret': "Test data?", "password": "qwerty"}).json()
    wrong_response = test_app.post(f'/secrets/gasdgasreg', json={'password': "123"})
    response = test_app.post(f'/secrets/{key}', json={'password': "qwerty"})
    assert response.status_code == 200
    assert response.json() == "Test data?"
    assert wrong_response.json() is None
