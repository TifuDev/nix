from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import UserIsBlocked

import aiohttp
import asyncio
import xmltodict

from src.config import logging
from src.config import config


@Client.on_message(filters.command("feed"))
async def feedCommand(_, message: Message):
    for channel in config["channels"]:
        notice = await get_new(channel)
        first_new = notice["item"][0]

        await message.reply(
            feed_template(
                title=first_new["title"],
                description=first_new["description"],
                channel_name=notice["title"],
                url=first_new["link"],
            )
        )


"""
Get channel information from URL
"""


async def get_new(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            return xmltodict.parse(await res.text())["rss"]["channel"]


"""
Formats new using template
"""


def feed_template(title, description, channel_name, url):
    return config["message"]["template"].format(
        title=title, description=description, channel_name=channel_name, url=url
    )
