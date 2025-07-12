from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.routes import ticket_route

app = FastAPI(title="Vierta", description="API for Vierta Tickets", version="0.1")

# DB Connection
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(ticket_route.router, prefix="/api/v1", tags=["ticket"])