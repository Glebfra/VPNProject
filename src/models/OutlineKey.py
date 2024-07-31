import os
from datetime import datetime

from sqlalchemy import DateTime, String, create_engine
from sqlalchemy.orm import Mapped, mapped_column

from src.models.Base import Base


class OutlineKey(Base):
    __tablename__ = 'outline_key'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[str] = mapped_column(String(256), nullable=True, default=None)
    name: Mapped[str] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(256))
    port: Mapped[str] = mapped_column(String(5))
    method: Mapped[str] = mapped_column(String(256))
    access_url: Mapped[str] = mapped_column(String(256))
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)


if __name__ == '__main__':
    engine = create_engine(os.getenv('SERVER_DB'), echo=True)
    OutlineKey.__table__.create(engine)
