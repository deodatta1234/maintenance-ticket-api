from fastapi.testclient import TestClient

from demo_service.api import app

client = TestClient(app)


def test_lists_all_tickets() -> None:
    response = client.get("/maintenance-tickets")
    assert response.status_code == 200
    assert len(response.json()) == 3
