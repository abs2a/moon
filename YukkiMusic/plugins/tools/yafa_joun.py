from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from config import YAFA_CHANNEL, YAFA_NAME, CHANNEL_SUDO
from YukkiMusic import app


@app.on_message(~filters.edited & filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not CHANNEL_SUDO:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(CHANNEL_SUDO, msg.from_user.id)
        except UserNotParticipant:
            if CHANNEL_SUDO.isalpha():
                link = u"{CHANNEL_SUDO}"
            else:
                chat_info = await bot.get_chat(CHANNEL_SUDO)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f" ⏺️꒐ عليك الاشتراك في قناة البوت اولاً •\n!! | اشترك ثم ارسل /start",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"{CHANNEL_SUDO}", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"عليك رفع البوت آدمن في القناة أولاً ؟؟ : {CHANNEL_SUDO} !")
