import pytest
from app import app, db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_login_missing_fields(client):
    response = client.post("/api/auth/login", json={})
    assert response.status_code == 400

def test_login_invalid_user(client):
    response = client.post("/api/auth/login", json={"username": "nobody", "password": "wrong"})
    assert response.status_code == 401

def test_register_short_password(client):
    response = client.post("/api/auth/register", json={
        "username": "test", "email": "test@test.com", "password": "123"
    })
    assert response.status_code == 400
