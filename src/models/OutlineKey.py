from datetime import datetime

from sqlalchemy import DateTime, String, create_engine
from sqlalchemy.orm import Mapped, mapped_column

from src.models.Base import Base


class OutlineKey(Base):
    __tablename__ = 'outline_key'

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)


if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://root:root@localhost/db', echo=True)
    OutlineKey.__table__.create(engine)
