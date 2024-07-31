import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


if __name__ == '__main__':
    engine = create_engine(os.getenv('SERVER_DB'), echo=True)
    Base.metadata.create_all(engine)
