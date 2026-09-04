# Maintenance Ticket API

Run `uvicorn demo_service.api:app --reload`.

## List maintenance tickets

To return all three existing tickets:

```http
GET /maintenance-tickets
```

To return only high-priority tickets (IDs 1 and 3):

```http
GET /maintenance-tickets?priority=high
```

To return only low-priority tickets (ID 2):

```http
GET /maintenance-tickets?priority=low
```

Supported priority values are `low`, `medium`, and `high`.
