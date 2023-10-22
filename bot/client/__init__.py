"""Creates the Discord bot client and registers any event handlers."""

from discord.ext.commands import Bot

from logger import logger


class TomNook(Bot):
    """The Discord bot client."""

    async def on_ready(self):
        """Called when the client is done preparing the data received from Discord."""
        logger.info(f"🚀 Ready! Logged on as {self.user}.")


client = TomNook()
