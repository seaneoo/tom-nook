import os
from typing import TypedDict

from dotenv import dotenv_values


class TypedConfig(TypedDict):
    DISCORD_BOT_TOKEN: str


config: TypedConfig = {
    **dotenv_values(".env"),
    **os.environ,
}
