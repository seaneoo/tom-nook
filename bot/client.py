"""Creates the Discord bot client and registers any event handlers."""

from discord import Client


class TomNook(Client):
    """The Discord bot client."""

    async def on_ready(self):
        """Called when the client is done preparing the data received from Discord."""
        print(f"🚀 Ready! Logged on as {self.user}.")


client = TomNook()
