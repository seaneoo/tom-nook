from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import Base

engine = create_engine("postgresql+psycopg://username:password@localhost:5432/tomnook")

Base.metadata.create_all(bind=engine)


def session() -> Session:
    """Constructs a new session using the database engine.

    Returns:
        Session: The ORM session.
    """
    return Session(engine)
