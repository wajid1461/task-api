from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "CI/CD Learning Project"
    }

def test_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 2