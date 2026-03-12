from __future__ import annotations
from datetime import datetime, UTC
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    age: Mapped[int] = mapped_column(Integer,nullable=False)
    city: Mapped[str] = mapped_column(String(100),nullable=False,index=True)
    registration_date: Mapped[datetime] = mapped_column(DateTime(timezone=True),default=lambda: datetime.now(UTC))
    password_hash: Mapped[str] = mapped_column(String(200), nullable=False)