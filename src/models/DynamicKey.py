from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, create_engine
from sqlalchemy.orm import Mapped, mapped_column

from src.models.Base import Base
from src.models.OutlineKey import OutlineKey


class DynamicKey(Base):
    __tablename__ = 'dynamic_key'

    id: Mapped[int] = mapped_column(primary_key=True)
    outline_key: Mapped[OutlineKey] = mapped_column(ForeignKey(OutlineKey.id))
    dynamic_outline_key: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)


if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://root:root@localhost/db', echo=True)
    DynamicKey.__table__.create(engine)
