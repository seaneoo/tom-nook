from discord import Client


class TomNook(Client):
    async def on_ready(self):
        print(f"🚀 Ready! Logged on as {self.user}.")


client = TomNook()
