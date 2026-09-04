from fastapi.testclient import TestClient

from demo_service.api import app

client = TestClient(app)


def test_lists_all_tickets() -> None:
    response = client.get("/maintenance-tickets")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "Inspect lift", "priority": "high"},
        {"id": 2, "title": "Replace light", "priority": "low"},
        {"id": 3, "title": "Service boiler", "priority": "high"},
    ]


def test_filters_high_priority_tickets() -> None:
    response = client.get("/maintenance-tickets", params={"priority": "high"})

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "Inspect lift", "priority": "high"},
        {"id": 3, "title": "Service boiler", "priority": "high"},
    ]


def test_filters_low_priority_tickets() -> None:
    response = client.get("/maintenance-tickets", params={"priority": "low"})

    assert response.status_code == 200
    assert response.json() == [
        {"id": 2, "title": "Replace light", "priority": "low"},
    ]


def test_filters_medium_priority_tickets() -> None:
    response = client.get("/maintenance-tickets", params={"priority": "medium"})

    assert response.status_code == 200
    assert response.json() == []


def test_rejects_unsupported_priority() -> None:
    response = client.get("/maintenance-tickets", params={"priority": "urgent"})

    assert response.status_code == 422


def test_gets_ticket_by_id() -> None:
    response = client.get("/maintenance-tickets/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Inspect lift",
        "priority": "high",
    }


def test_returns_not_found_for_missing_ticket() -> None:
    response = client.get("/maintenance-tickets/999")

    assert response.status_code == 404
