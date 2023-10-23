from typing import TYPE_CHECKING

from sqlalchemy.dialects.postgresql import insert

from common.logger import logger

from .models import Guild

if TYPE_CHECKING:
    from discord import Guild as DiscordGuild
    from sqlalchemy.orm import Session


def insert_guilds(session: "Session", *guilds: "DiscordGuild"):
    """Insert n Discord guilds into the database.

    Args:
        session (Session): The ORM session.
    """
    with session as s:
        try:
            # Map each Discord guild to a Guild ORM object
            guild_orms = [
                Guild(
                    guild_id=guild.id,
                    channel_id=guild.system_channel.id
                    if guild.system_channel
                    else None,
                )
                for guild in guilds
            ]
            # Get the column values for each Guild ORM object
            guild_values = [
                {
                    key: value
                    for key, value in guild.__dict__.items()
                    if key != "_sa_instance_state"
                }
                for guild in guild_orms
            ]
            # Create the SQL statement
            statement = (
                insert(Guild.__table__)
                .values(guild_values)
                .on_conflict_do_nothing(index_elements=["guild_id"])
            )
            # Execute the SQL statement and commit the changes
            s.execute(statement)
            s.commit()
        except Exception as e:
            logger.err(e)


def select_all_guilds(session: "Session") -> list[Guild]:
    with session as s:
        try:
            return s.query(Guild).all()
        except Exception as e:
            logger.err(e)


def select_guild(session: "Session", guild: "DiscordGuild") -> Guild | None:
    with session as s:
        try:
            return s.query(Guild).filter(Guild.guild_id == str(guild.id)).first()
        except Exception as e:
            logger.err(e)
