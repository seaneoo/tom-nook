from typing import TYPE_CHECKING

from sqlalchemy.dialects.postgresql import insert

from common.logger import logger

from .models import Guild

if TYPE_CHECKING:
    from discord import Guild as DiscordGuild
    from sqlalchemy.orm import Session


def insert_guilds(session: "Session", *discord_guilds: "DiscordGuild"):
    with session as s:
        try:
            guilds = [
                Guild(
                    guild_id=dg.id,
                    channel_id=dg.system_channel.id if dg.system_channel else None,
                )
                for dg in discord_guilds
            ]

            statement = (
                insert(Guild)
                .values([guild.to_dict() for guild in guilds])
                .on_conflict_do_nothing(index_elements=["guild_id"])
            )

            s.execute(statement)
            s.commit()
        except Exception as e:
            logger.err(e)


def select_all_guilds(session: "Session") -> list[Guild] | None:
    with session as s:
        try:
            return s.query(Guild).all()
        except Exception as e:
            logger.err(e)


def select_guild(session: "Session", discord_guild: "DiscordGuild") -> Guild | None:
    with session as s:
        try:
            return (
                s.query(Guild).filter(Guild.guild_id == str(discord_guild.id)).first()
            )
        except Exception as e:
            logger.err(e)
