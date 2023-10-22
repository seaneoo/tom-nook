"""Main entry point for the application and runs the Discord bot client."""

from bot.client import client
from bot.config import config

TOKEN = config["DISCORD_BOT_TOKEN"]
client.run(TOKEN)
