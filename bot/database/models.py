from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import registry
from sqlalchemy.orm.decl_api import DeclarativeMeta

mapper_registry = registry()


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True
    registry = mapper_registry
    metadata = mapper_registry.metadata

    __init__ = mapper_registry.constructor


class Guild(Base):
    __tablename__ = "guilds"

    guild_id = Column(String, primary_key=True)
    channel_id = Column(String, nullable=True, default=None)
    last_sent = Column(DateTime, nullable=True, default=None)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self) -> str:
        """
        Returns:
            str: Representation of the Guild model and each of its attributes.
        """
        return f"<Guild guild_id='{self.guild_id}' channel_id='{self.channel_id}' last_sent='{self.last_sent}' created_at='{self.created_at}'>"

    def __str__(self) -> str:
        """
        Returns:
            str: Human-readable representation of the Guild model.
        """
        return f"Guild ID# {self.guild_id}"

    def to_dict(self) -> dict[str, Any]:
        """
        Returns:
            dict[str, Any]: Dictionary representation of the Guild model without the '_sa_instance_state' attribute.
        """
        return {
            key: value
            for key, value in self.__dict__.items()
            if key != "_sa_instance_state"
        }
