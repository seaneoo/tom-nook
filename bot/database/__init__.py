from datetime import datetime

from sqlalchemy import Column, DateTime, String, Table, create_engine
from sqlalchemy.orm import Session, registry
from sqlalchemy.orm.decl_api import DeclarativeMeta

mapper_registry = registry()


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True
    registry = mapper_registry
    metadata = mapper_registry.metadata

    __init__ = mapper_registry.constructor


class Guild(Base):
    __table__ = Table(
        "Guilds",
        Base.metadata,
        Column("GuildID", String, primary_key=True),
        Column("CreatedAt", DateTime, default=datetime.now()),
    )

    def __init__(self, guild_id):
        self.guild_id = guild_id


engine = create_engine("postgresql+psycopg://username:password@localhost:5432/tomnook")

Base.metadata.create_all(bind=engine)


def session() -> Session:
    """Constructs a new session using the database engine.

    Returns:
        Session: The ORM session.
    """
    return Session(engine)
