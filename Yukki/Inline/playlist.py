from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data="close")
        ],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [   InlineKeyboardButton(
                text=f"✨Cᴍᴅs⚡",
                url="https://telegra.ph/%E1%B4%85%E1%B4%87%E1%B4%A0%E1%B4%9CMusic-02-11",
            ),
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ💫",
                url="https://t.me/insane_bots",
            ),
        ],
        [
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data="close")
        ],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ʙᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"play_playlist {user_id}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"ʜᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"play_playlist {user_id}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴀʀᴛʏ",
                callback_data=f"play_playlist {user_id}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"ʟᴏꜰɪ",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"sᴀᴅ",
                callback_data=f"play_playlist {user_id}|{type}|Sad",
            ),
            InlineKeyboardButton(
                text=f"ᴡᴇᴇʙ",
                callback_data=f"play_playlist {user_id}|{type}|Weeb",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴜɴᴊᴀʙɪ",
                callback_data=f"play_playlist {user_id}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"ᴏᴛʜᴇʀs",
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="«ɢᴏ-ʙᴀᴄᴋ",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ ᴡᴇᴇʙ",
                callback_data=f"add_playlist {videoid}|{type}|Weeb",
            ),
            InlineKeyboardButton(
                text=f"✚ sᴀᴅ",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ᴘᴀʀᴛʏ",
                callback_data=f"add_playlist {videoid}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"✚ ʟᴏꜰɪ",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ʙᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"add_playlist {videoid}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"✚ ʜᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"add_playlist {videoid}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ᴘᴜɴᴊᴀʙɪ",
                callback_data=f"add_playlist {videoid}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"✚ ᴏᴛʜᴇʀs",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="«ɢᴏ-ʙᴀᴄᴋ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="×ᴄʟᴏsᴇ×", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ᴡᴇᴇʙ", callback_data=f"check_playlist {type}|Weeb"
            ),
            InlineKeyboardButton(
                text=f"sᴀᴅ", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴀʀᴛʏ", callback_data=f"check_playlist {type}|Party"
            ),
            InlineKeyboardButton(
                text=f"ʟᴏꜰɪ", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ʙᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"ʜᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴜɴᴊᴀʙɪ",
                callback_data=f"check_playlist {type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"ᴏᴛʜᴇʀs", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ɢʀᴏᴜᴘ's",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="ǫᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪsᴛ", url=f"{url}")],
        [InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="ᴄʜᴇᴄᴋᴏᴜᴛ ᴘʟᴀʏʟɪsᴛ", url=f"{url}")],
        [InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Yes! Delete",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="No!", callback_data=f"close"),
        ],
    ]
    return buttons
