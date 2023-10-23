from datetime import datetime

from sqlalchemy import Column, DateTime, String, Table
from sqlalchemy.orm import registry
from sqlalchemy.orm.decl_api import DeclarativeMeta

mapper_registry = registry()


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True
    registry = mapper_registry
    metadata = mapper_registry.metadata

    __init__ = mapper_registry.constructor


class Guild(Base):
    __table__ = Table(
        "guilds",
        Base.metadata,
        Column("guild_id", String, primary_key=True),  # The unique ID for the guild
        Column(
            "channel_id", String, nullable=True, default=None
        ),  # The ID of the guild's channel to send messages in
        Column(
            "last_sent", DateTime, nullable=True, default=None
        ),  # The timestamp the birthday message was last sent
        Column(
            "created_at", DateTime, default=datetime.now()
        ),  # The timestamp the row was created
    )

    def __init__(self, guild_id, channel_id):
        self.guild_id = guild_id
        self.channel_id = channel_id
