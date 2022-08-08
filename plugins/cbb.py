#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>MASTER</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://t.me/linkzofallmygroups'>Click here</a>\n○ Channel : @linkzofallmygroups\n○ Support Group : @supprotosfmebot</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close"),
                        InlineKeyboardButton('👩‍🦯 Back', callback_data='back'),
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()

    elif CallbackQuery.data == "back"
        CallbackQuery.edit_message_text(START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
             reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🧩 About 🧩", callback_data = "about"),
                    InlineKeyboardButton("🍀 Close 🍀", callback_data = "close"),
                ],[
                    InlineKeyboardButton("🔅 GROUP 🔅", url = "https://t.me/+IUjmXAy5pVg1MDQ1") 
                ]
            ]
        )
        except:
            pass
