from sqlalchemy.orm import Session
import pandas as pd
from app import models


def get_average_age(db: Session) -> float:
    users = db.query(models.User).all()
    if not users:
        return 0.0
    df = pd.DataFrame([
        {"age": u.age} for u in users
        ])
    return df["age"].mean()


def get_users_per_city(db: Session) -> dict:
    users = db.query(models.User).all()
    if not users:
        return {}
    df = pd.DataFrame([{"city": u.city} for u in users])
    return df["city"].value_counts().to_dict()