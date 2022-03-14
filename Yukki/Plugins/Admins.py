import asyncio
import os
import random
from asyncio import QueueEmpty

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton, Message,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)

from config import get_queue
from Yukki import BOT_USERNAME, MUSIC_BOT_NAME, app, db_mem
from Yukki.Core.PyTgCalls import Queues
from Yukki.Core.PyTgCalls.Converter import convert
from Yukki.Core.PyTgCalls.Downloader import download
from Yukki.Core.PyTgCalls.Yukki import (pause_stream, resume_stream,
                                        skip_stream, stop_stream)
from Yukki.Database import (is_active_chat, is_music_playing, music_off,
                            music_on, remove_active_chat)
from Yukki.Decorators.admins import AdminRightsCheck
from Yukki.Decorators.checker import checker, checkerCB
from Yukki.Inline import (audio_markup, audio_markup2, audio_markup202, download_markup,
                          fetch_playlist, paste_queue_markup, primary_markup)
from Yukki.Utilities.changers import time_to_seconds
from Yukki.Utilities.chat import specialfont_to_normal
from Yukki.Utilities.theme import check_theme
from Yukki.Utilities.thumbnails import gen_thumb
from Yukki.Utilities.timer import start_timer
from Yukki.Utilities.youtube import get_yt_info_id

loop = asyncio.get_event_loop()


__MODULE__ = "Voice Chat"
__HELP__ = """


/pause
- Pause the playing music on voice chat.

/resume
- Resume the paused music on voice chat.

/skip
- Skip the current playing music on voice chat

/end or /stop
- Stop the playout.

/queue
- Check queue list.


**Note:**
Only for Sudo Users

/activevc
- Check active voice chats on bot.

"""
PLAY_PAUSED = "https://telegra.ph/file/37d4ea97e97877eb63f93.jpg"
PLAY_ENDED = "https://telegra.ph/file/eb33b1f0daaecb911d013.jpg"
PLAY_RESUMED = "https://telegra.ph/file/4e65d111fdb89809fe94e.jpg"
#PLAY_SKIPED = "https://telegra.ph/file/78189a482f76fdc3f8185.jpg"
PLAY_EMPTY = "https://telegra.ph/file/71abca6d0b300685a25e6.jpg"

@app.on_message(
    filters.command(["pause", "skip", "resume", "stop", "end"])
    & filters.group
)
@AdminRightsCheck
@checker
async def admins(_, message: Message):
    global get_queue
    if not len(message.command) == 1:
        return await message.reply_text("Error! Wrong Usage of Command.")
    if not await is_active_chat(message.chat.id):
        return await message.reply_text("Nothing is playing on voice chat.")
    chat_id = message.chat.id
    if message.command[0][1] == "a":
        if not await is_music_playing(message.chat.id):
            return await message.reply_text("Music is already Paused.")
        await music_off(chat_id)
        await pause_stream(chat_id)
        await message.reply_photo(PLAY_PAUSED,
            caption= f"🎧 ᴠᴏɪᴄᴇᴄʜᴀᴛ ᴘᴀᴜsᴇᴅ ʙʏ {message.from_user.mention}!\n\n✘ /resume :- ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ ᴀɢᴀɪɴ!!!✨",
            reply_markup=audio_markup202,
        )
    if message.command[0][1] == "e":
        if await is_music_playing(message.chat.id):
            return await message.reply_text("Music is already Playing.")
        await music_on(chat_id)
        await resume_stream(chat_id)
        await message.reply_photo(PLAY_RESUMED,
            caption= f"🎧 ᴠᴏɪᴄᴇᴄʜᴀᴛ ʀᴇsᴜᴍᴇᴅ ʙʏ {message.from_user.mention}!\n\n✘ /pause :- ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛʀᴇᴀᴍ!!!✨",
            reply_markup=audio_markup202,
        )
    if message.command[0][1] == "t" or message.command[0][1] == "n":
        try:
            Queues.clear(message.chat.id)
        except QueueEmpty:
            pass
        await remove_active_chat(chat_id)
        await stop_stream(chat_id)
        await message.reply_photo(PLAY_ENDED,
            caption= f"🎧 ᴠᴏɪᴄᴇᴄʜᴀᴛ ᴇɴᴅᴇᴅ ʙʏ {message.from_user.mention}!\n\nʙʏᴇ ʙʏᴇ, ʟᴇᴀᴠɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ!!!✨",
            reply_markup=audio_markup202,
        )
    if message.command[0][1] == "k":
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await message.reply_photo(PLAY_EMPTY,
                caption= "ɴᴏ ᴍᴏʀᴇ ᴍᴜsɪᴄ ɪɴ __ǫᴜᴇᴜᴇ__ \n\nʟᴇᴀᴠɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ",
                reply_markup=audio_markup202,
            )
            await stop_stream(chat_id)
            return
        else:
            videoid = Queues.get(chat_id)["file"]
            got_queue = get_queue.get(chat_id)
            if got_queue:
                got_queue.pop(0)
            finxx = f"{videoid[0]}{videoid[1]}{videoid[2]}"
            aud = 0
            if str(finxx) != "raw":
                mystic = await message.reply_text(
                    f"**{MUSIC_BOT_NAME} ᴘʟᴀʏʟɪsᴛ ꜰᴜɴᴄᴛɪᴏɴ**\n\n__ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɴᴇxᴛ ᴍᴜsɪᴄ ꜰʀᴏᴍ ᴘʟᴀʏʟɪsᴛ....__"
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(videoid)
                await mystic.edit(
                    f"**{MUSIC_BOT_NAME} ᴅᴏᴡɴʟᴏᴀᴅᴇʀ**\n\n**ᴛɪᴛʟᴇ:** {title[:50]}\n\n0% ____________ 100%"
                )
                downloaded_file = await loop.run_in_executor(
                    None, download, videoid, mystic, title
                )
                raw_path = await convert(downloaded_file)
                await skip_stream(chat_id, raw_path)
                theme = await check_theme(chat_id)
                chat_title = await specialfont_to_normal(message.chat.title)
                thumb = await gen_thumb(
                    thumbnail, title, message.from_user.id, theme, chat_title
                )
                buttons = primary_markup(
                    videoid, message.from_user.id, duration_min, duration_min
                )
                await mystic.delete()
                mention = db_mem[videoid]["username"]
                final_output = await message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=(
                        f"<b>__sᴋɪᴘᴇᴅ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ__</b>\n\n♫︎<b>__sᴛᴀʀᴛᴇᴅ ᴘʟᴀʏɪɴɢ:__ </b>[{title[:25]}](https://www.youtube.com/watch?v={videoid}) \n⏳<b>__ᴅᴜʀᴀᴛɪᴏɴ:__</b> {duration_min} Mins\n🧚‍♀️**__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__** {mention}"
                    ),
                )
                os.remove(thumb)
            else:
                await skip_stream(chat_id, videoid)
                afk = videoid
                title = db_mem[videoid]["title"]
                duration_min = db_mem[videoid]["duration"]
                duration_sec = int(time_to_seconds(duration_min))
                mention = db_mem[videoid]["username"]
                videoid = db_mem[videoid]["videoid"]
                if str(videoid) == "smex1":
                    buttons = buttons = audio_markup(
                        videoid,
                        message.from_user.id,
                        duration_min,
                        duration_min,
                    )
                    thumb = "https://telegra.ph/file/9cc8f3b1a0751f6b27553.png"
                    aud = 1
                else:
                    _path_ = _path_ = (
                        (str(afk))
                        .replace("_", "", 1)
                        .replace("/", "", 1)
                        .replace(".", "", 1)
                    )
                    thumb = f"cache/{_path_}final.png"
                    buttons = primary_markup(
                        videoid,
                        message.from_user.id,
                        duration_min,
                        duration_min,
                    )
                final_output = await message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"<b>__sᴋɪᴘᴘᴇᴅ ᴠᴄ__</b>\n\n♫︎<b>__sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ:__</b> {title} \n⏳<b>__ᴅᴜʀᴀᴛɪᴏɴ:__</b> {duration_min} \n🧚‍♀️<b>__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__ </b> {mention}",
                )
            await start_timer(
                videoid,
                duration_min,
                duration_sec,
                final_output,
                message.chat.id,
                message.from_user.id,
                aud,
            )
