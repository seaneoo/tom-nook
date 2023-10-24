from discord import Guild, Intents
from discord.ext.commands import Bot

from bot.database import session
from bot.database.helpers import insert_guilds
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
        insert_guilds(session(), *self.guilds)

    async def on_guild_join(self, guild: Guild):
        """Called when the client joins a guild."""
        insert_guilds(session(), guild)
        logger.info(f"Joined Guild ID# {guild.id}")


intents = Intents.default()
intents.guilds = True

client = TomNook(intents=intents)
