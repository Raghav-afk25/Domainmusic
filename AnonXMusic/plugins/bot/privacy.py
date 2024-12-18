from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.enums import ParseMode
from AnonXMusic import app
import config

TEXT = f"""
🔒 **Privacy Policy for Bot Hub Bot's !**
"""

@app.on_message(filters.command("privacy"))
async def privacy(client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "View Privacy Policy", url=f"http://telegra.ph/BOT-HUB-MUSIC-BOT-PRIVACY-POLICY-12-18"
                )
            ]
        ]
    )
    await message.reply_text(
        TEXT, 
        reply_markup=keyboard, 
        parse_mode=ParseMode.MARKDOWN, 
        disable_web_page_preview=True
    )
