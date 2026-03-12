from fastapi import FastAPI
from app.routers import users, analytics
from app.database import engine, Base

api = FastAPI(
    title="API",
    description="API REST per gestione utenti e analisi dati",
    version="0.1.0"
)

api.include_router(users.router)
api.include_router(analytics.router)


@api.get("/")
def root():
    return {"message": "attivo"}