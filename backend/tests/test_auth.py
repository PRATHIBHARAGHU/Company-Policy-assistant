import os
import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

os.environ.setdefault("DATABASE_URL", "sqlite:///./test_app.db")
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("ALGORITHM", "HS256")
os.environ.setdefault("ACCESS_TOKEN_EXPIRE_MINUTES", "30")

from app.main import app

client = TestClient(app)


def test_register_and_login_flow():
    response = client.post(
        "/auth/register",
        json={
            "email": "employee@example.com",
            "username": "employee",
            "password": "Password123!",
            "role": "employee",
        },
    )
    assert response.status_code == 201

    login_response = client.post(
        "/auth/login",
        data={"username": "employee@example.com", "password": "Password123!"},
    )
    assert login_response.status_code == 200
    payload = login_response.json()
    assert payload["access_token"]
    assert payload["token_type"] == "bearer"
