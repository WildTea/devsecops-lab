import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    data = r.get_json()
    assert "message" in data