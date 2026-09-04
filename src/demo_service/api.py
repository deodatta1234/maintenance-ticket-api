from fastapi import FastAPI, HTTPException

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


@app.get("/maintenance-tickets/{ticket_id}", response_model=MaintenanceTicket)
def get_maintenance_ticket(ticket_id: int) -> MaintenanceTicket:
    """Return a maintenance ticket by ID."""
    for ticket in TICKETS:
        if ticket.id == ticket_id:
            return ticket
    raise HTTPException(status_code=404, detail="Maintenance ticket not found")
