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

## Get a maintenance ticket by ID

To return the ticket with ID 1:

```http
GET /maintenance-tickets/1
```

Successful response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id":1,"title":"Inspect lift","priority":"high"}
```

If the ticket does not exist:

```http
GET /maintenance-tickets/999
```

Missing-ticket response:

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{"detail":"Maintenance ticket not found"}
```
