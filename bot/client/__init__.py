from discord.ext.commands import Bot
from sqlalchemy.dialects.postgresql import insert

from bot.database import Guild, session
from common.logger import logger

commands = ["ping"]


class TomNook(Bot):
    """The Discord bot client."""

    def __init__(self, **options):
        super().__init__(**options)

        for c in commands:
            path = f"bot.client.commands.{c}"
            self.load_extension(path)
            logger.info(f'Loaded command "{path}".')

    async def on_ready(self):
        """Called when the client is done preparing the data received from Discord."""
        logger.info(f"🚀 Ready! Logged on as {self.user}.")

        # TODO: Move this functionality elsewhere
        with session() as sess:
            """Inserts any guilds into the database that were not already added
            (this is used for if the bot joins a guild while it was offline)."""
            try:
                guilds = [
                    Guild(guild_id=guild.id, channel_id=guild.system_channel.id)
                    for guild in self.guilds
                ]

                statement = (
                    insert(Guild.__table__)
                    .values(
                        [
                            {
                                key: value
                                for key, value in guild.__dict__.items()
                                if key != "_sa_instance_state"
                            }
                            for guild in guilds
                        ]
                    )
                    .on_conflict_do_nothing(
                        index_elements=["guild_id"],
                    )
                )

                sess.execute(statement)
                sess.commit()
            except Exception as e:
                logger.err(e)


client = TomNook()
