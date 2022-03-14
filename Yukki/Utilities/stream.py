import asyncio
import os
import shutil

from pyrogram.types import InlineKeyboardMarkup

from config import get_queue
from Yukki import BOT_USERNAME, db_mem
from Yukki.Core.PyTgCalls import Queues
from Yukki.Core.PyTgCalls.Yukki import join_stream
from Yukki.Database import (add_active_chat, is_active_chat, music_off,
                            music_on)
from Yukki.Inline import (audio_markup, audio_markup2, primary_markup,
                          secondary_markup)
from Yukki.Utilities.timer import start_timer

loop = asyncio.get_event_loop()


async def start_stream(
    CallbackQuery,
    file,
    videoid,
    thumb,
    title,
    duration_min,
    duration_sec,
    mystic,
):
    global get_queue
    if await is_active_chat(CallbackQuery.message.chat.id):
        position = await Queues.put(CallbackQuery.message.chat.id, file=file)
        _path_ = (
            (str(file))
            .replace("_", "", 1)
            .replace("/", "", 1)
            .replace(".", "", 1)
        )
        buttons = secondary_markup(videoid, CallbackQuery.from_user.id)
        if file not in db_mem:
            db_mem[file] = {}
        cpl = f"cache/{_path_}final.png"
        shutil.copyfile(thumb, cpl)
        wtfbro = db_mem[file]
        wtfbro["title"] = title
        wtfbro["duration"] = duration_min
        wtfbro["username"] = CallbackQuery.from_user.mention
        wtfbro["videoid"] = videoid
        got_queue = get_queue.get(CallbackQuery.message.chat.id)
        title = title
        user = CallbackQuery.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        final_output = await CallbackQuery.message.reply_photo(
            photo=thumb,
            caption=(
                f"🎬<u>__sᴏɴɢ:__ </u>[{title[:25]}](https://www.youtube.com/watch?v={videoid}) \n⏳<b>__ᴅᴜʀᴀᴛɪᴏɴ:__</b> {duration_min} \n🤍<b>__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__ </b>{CallbackQuery.from_user.mention} \n🧚‍♀️<b>__ǫᴜᴇᴜᴇᴅ ᴀᴛ:__</b> <b>#{position}!</b>\n\n<u><i>➬➬ Pᴏᴡᴇʀᴇᴅ Bʏ Cᴏɴᴛʀᴏʟʟᴇʀ [Tᴇᴀᴍ-Sɪʟᴇɴᴛ💞](t.me/SILENT_DEVS) ✨</i></u>"
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        await mystic.delete()
        await CallbackQuery.message.delete()
        os.remove(thumb)
        return
    else:
        if not await join_stream(CallbackQuery.message.chat.id, file):
            return await mystic.edit(
                "ᴇʀʀᴏʀ ᴊᴏɪɴɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. ᴍᴀᴋᴇ sᴜʀᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪs ᴇɴᴀʙʟᴇᴅ."
            )
        get_queue[CallbackQuery.message.chat.id] = []
        got_queue = get_queue.get(CallbackQuery.message.chat.id)
        title = title
        user = CallbackQuery.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        await music_on(CallbackQuery.message.chat.id)
        await add_active_chat(CallbackQuery.message.chat.id)
        buttons = primary_markup(
            videoid, CallbackQuery.from_user.id, duration_min, duration_min
        )
        await mystic.delete()
        cap = f"🎵<u>__ᴘʟᴀʏɪɴɢ:__ </u>[{title[:25]}](https://www.youtube.com/watch?v={videoid}) \n🧚‍♀️**__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__** {CallbackQuery.from_user.mention} \n\n<u><i>➬➬ Pᴏᴡᴇʀᴇᴅ Bʏ Cᴏɴᴛʀᴏʟʟᴇʀ [Tᴇᴀᴍ-Sɪʟᴇɴᴛ💞](t.me/SILENT_DEVS) ✨</i></u>"
        final_output = await CallbackQuery.message.reply_photo(
            photo=thumb,
            reply_markup=InlineKeyboardMarkup(buttons),
            caption=cap,
        )
        os.remove(thumb)
        await CallbackQuery.message.delete()
        await start_timer(
            videoid,
            duration_min,
            duration_sec,
            final_output,
            CallbackQuery.message.chat.id,
            CallbackQuery.from_user.id,
            0,
        )


async def start_stream_audio(
    message, file, videoid, title, duration_min, duration_sec, mystic
):
    global get_queue
    if message.chat.username:
        link = f"https://t.me/{message.chat.username}/{message.reply_to_message.message_id}"
    else:
        xf = str((message.chat.id))[4:]
        link = f"https://t.me/c/{xf}/{message.reply_to_message.message_id}"
    if await is_active_chat(message.chat.id):
        position = await Queues.put(message.chat.id, file=file)
        if file not in db_mem:
            db_mem[file] = {}
        db_mem[file]["title"] = title
        db_mem[file]["duration"] = duration_min
        db_mem[file]["username"] = message.from_user.mention
        db_mem[file]["videoid"] = videoid
        got_queue = get_queue.get(message.chat.id)
        title = title
        user = message.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        final_output = await message.reply_photo(
            photo="https://telegra.ph/file/9cc8f3b1a0751f6b27553.png",
            caption=(
                f"🎬<b>__ᴀᴜᴅɪᴏ:__ </b> [ᴀᴜᴅɪᴏ ɢɪᴠᴇɴ ᴠᴀɪ ᴛɢ]({link})\n⏳<b>__ᴅᴜʀᴀᴛɪᴏɴ:__</b> {duration_min} \n🤍<b>__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__ </b>{message.from_user.mention} \n🧚‍♀️<b>__ǫᴜᴇᴜᴇᴅ ᴀᴛ:__</b> <b>#{position}!</b> \n\n<u><i>➬➬ Pᴏᴡᴇʀᴇᴅ Bʏ Cᴏɴᴛʀᴏʟʟᴇʀ [Tᴇᴀᴍ-Sɪʟᴇɴᴛ💞](t.me/SILENT_DEVS) ✨</i></u>"
            ),
            reply_markup=audio_markup2,
        )
        await mystic.delete()
        return
    else:
        if not await join_stream(message.chat.id, file):
            return await mystic.edit(
                "ᴇʀʀᴏʀ ᴊᴏɪɴɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. ᴍᴀᴋᴇ sᴜʀᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪs ᴇɴᴀʙʟᴇᴅ."
            )
        get_queue[message.chat.id] = []
        got_queue = get_queue.get(message.chat.id)
        title = title
        user = message.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        await music_on(message.chat.id)
        await add_active_chat(message.chat.id)
        buttons = audio_markup(
            videoid, message.from_user.id, duration_min, duration_min
        )
        await mystic.delete()
        cap = f"🎵<b>__ᴘʟᴀʏɪɴɢ:__ </b>[ᴀᴜᴅɪᴏ ɢɪᴠᴇɴ ᴠᴀɪ ᴛɢ]({link})\n🎬**__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__** {message.from_user.mention} \n\n<u><i>➬➬ Pᴏᴡᴇʀᴇᴅ Bʏ Cᴏɴᴛʀᴏʟʟᴇʀ [Tᴇᴀᴍ-Sɪʟᴇɴᴛ💞](t.me/SILENT_DEVS) ✨</i></u>"
        final_output = await message.reply_photo(
            photo="https://telegra.ph/file/9cc8f3b1a0751f6b27553.png",
            reply_markup=InlineKeyboardMarkup(buttons),
            caption=cap,
        )
        await start_timer(
            videoid,
            duration_min,
            duration_sec,
            final_output,
            message.chat.id,
            message.from_user.id,
            1,
        )
