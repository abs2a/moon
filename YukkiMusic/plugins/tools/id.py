import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#########
#الاوامر
@app.on_message(
    filters.command(["ايددي","ivvvvhgjd"],""))
async def vambir(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text(       f"""˖ : iD:  `{message.from_user.id}`\n\n˖ : iD: `{message.chat.id}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "𝖬𝗒 𝖲𝖳𝗎𝖿𝖿", url=f"https://t.me/uzzdd"),
                ],
                [  
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
