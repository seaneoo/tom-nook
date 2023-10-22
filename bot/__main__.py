from bot.client import client
from bot.config import config

TOKEN = config["DISCORD_BOT_TOKEN"]
client.run(TOKEN)
