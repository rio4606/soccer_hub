from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Добро пожаловать на Soccer Hub"}

def test_create_team():
    response = client.post("/teams/", json={"name": "Team A", "city": "City A", "founded_year": 2020})
    assert response.status_code == 200
    assert response.json()["name"] == "Team A"
