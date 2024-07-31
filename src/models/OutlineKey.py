from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.Base import Base


class OutlineKey(Base):
    __tablename__ = 'outline_key'

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)
