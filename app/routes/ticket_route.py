from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.ticket_schema import Ticket, TicketCreate
from app.controller.ticket_controller import (
    get_all_tickets,
    get_ticket,
    create_ticket,
    update_ticket,
    delete_ticket,
)

router = APIRouter(prefix="/tickets", tags=["Tickets"])

# List all tickets
@router.get("/", response_model=List[Ticket])
def list_tickets(db: Session = Depends(get_db)):
    return get_all_tickets(db)

# Create a new ticket
@router.post("/", response_model=Ticket)
def create_ticket_endpoint(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(db, ticket)

# Retrieve a ticket by its ID
@router.get("/{ticket_id}", response_model=Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

# Update an existing ticket by ID
@router.put("/{ticket_id}", response_model=Ticket)
def update_ticket_endpoint(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    updated = update_ticket(db, ticket_id, ticket)
    if not updated:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return updated

# Delete a ticket by ID
@router.delete("/{ticket_id}")
def delete_ticket_endpoint(ticket_id: int, db: Session = Depends(get_db)):
    if not delete_ticket(db, ticket_id):
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Ticket deleted"}
