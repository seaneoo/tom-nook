"""Defines the default config and environment variables used during runtime."""

import os
from typing import TypedDict

from dotenv import dotenv_values


class TypedConfig(TypedDict):
    """Environment variables that are needed during app runtime execution."""

    DISCORD_BOT_TOKEN: str


config: TypedConfig = {
    **dotenv_values(".env"),
    **os.environ,
}
