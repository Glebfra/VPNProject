from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://root:root@localhost/db', echo=True)
    Base.metadata.create_all(engine)
