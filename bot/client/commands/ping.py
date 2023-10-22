"""Creates and registers the ping command."""

from typing import TYPE_CHECKING

from discord import (  # pylint: disable = no-name-in-module
    ApplicationContext,
    slash_command,
)
from discord.ext import commands

if TYPE_CHECKING:
    from bot.client import TomNook


class PingCommand(commands.Cog):
    """A command to check the latency (delay) between the bot and server."""

    def __init__(self, client: "TomNook") -> None:
        self.client = client

    @slash_command(name="ping")
    async def ping_command(self, ctx: ApplicationContext):
        """Checks the latency (delay) between the bot and the server."""
        await ctx.respond(f"{(self.client.latency * 1000):.2f} ms")


def setup(client: "TomNook"):
    """Add the command (cog) to the client instance.

    Args:
        client (TomNook): The client instance.
    """
    client.add_cog(PingCommand(client))
