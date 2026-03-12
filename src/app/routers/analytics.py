from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database
from app.service import calculator

router = APIRouter(prefix="/analytics",tags=["analytics"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/average-age")
def average_age(db: Session = Depends(get_db)):
    return {"average_age": calculator.get_average_age(db)}


@router.get("/users-per-city")
def users_per_city(db: Session = Depends(get_db)):
    return calculator.get_users_per_city(db)