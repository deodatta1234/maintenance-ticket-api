from fastapi import FastAPI

from demo_service.models import MaintenanceTicket, Priority

app = FastAPI(title="Maintenance Ticket API")

TICKETS = [
    MaintenanceTicket(id=1, title="Inspect lift", priority=Priority.high),
    MaintenanceTicket(id=2, title="Replace light", priority=Priority.low),
    MaintenanceTicket(id=3, title="Service boiler", priority=Priority.high),
]


@app.get("/maintenance-tickets", response_model=list[MaintenanceTicket])
def list_maintenance_tickets(
    priority: Priority | None = None,
) -> list[MaintenanceTicket]:
    """List maintenance tickets, optionally filtered by priority."""
    if priority is None:
        return TICKETS
    return [ticket for ticket in TICKETS if ticket.priority == priority]
