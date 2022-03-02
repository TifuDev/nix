"""Starts Pyrogram client."""
from pyrogram import Client
from .config import SESSION_NAME, API_ID, API_HASH, TOKEN

# Information about this code can be found at https://docs.pyrogram.org/api/client

app = Client(
    session_name=SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins={"root": "src/plugins"},
)
