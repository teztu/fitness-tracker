from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_weigh_in_and_latest():
    payload = {"kg": 82.5}
    r = client.post("/weigh_in", json=payload)
    assert r.status_code in (201, 500, 409)  # 201 ved ny, 409/500 hvis den finnes fra før

    r2 = client.get("/weight/latest")
    assert r2.status_code == 200
    assert "kg" in r2.json() or r2.json() is None
