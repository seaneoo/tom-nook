from discord.ext.commands import Bot

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


client = TomNook()
