from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem



#url_markup2
def url_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="««",
                callback_data=f"slider B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="♫︎ᴘʟᴀʏ♫︎",
                callback_data=f"Yukki {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="»»",
                callback_data=f"slider F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="☦︎ᴍᴏʀᴇ",
                callback_data=f"Search {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="×ᴄʟᴏsᴇ×",
                callback_data=f"forceclose {query}|{user_id}",
            ),
        ],
    ]
    return buttons

'''
def url_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="▶️𝗣𝗟𝗔𝗬𝄞!",
                callback_data=f"Yukki {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑𝗖𝗟𝗢𝗦𝗘",
                callback_data=f"forceclose {query}|{user_id}",
            ),
        ],
    ]
    return buttons
'''

def search_markup(
    ID1,
    ID2,
    ID3,
    ID4,
    ID5,
    duration1,
    duration2,
    duration3,
    duration4,
    duration5,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="1", callback_data=f"Yukki {ID1}|{duration1}|{user_id}"
            ),
            InlineKeyboardButton(
                text="2", callback_data=f"Yukki {ID2}|{duration2}|{user_id}"
            ),
            InlineKeyboardButton(
                text="3", callback_data=f"Yukki {ID3}|{duration3}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="4", callback_data=f"Yukki {ID4}|{duration4}|{user_id}"
            ),
            InlineKeyboardButton(
                text="5", callback_data=f"Yukki {ID5}|{duration5}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="««", callback_data=f"popat 1|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="🗑ᴄʟᴏsᴇ", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="»»", callback_data=f"popat 1|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def search_markup2(
    ID6,
    ID7,
    ID8,
    ID9,
    ID10,
    duration6,
    duration7,
    duration8,
    duration9,
    duration10,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="6",
                callback_data=f"Yukki {ID6}|{duration6}|{user_id}",
            ),
            InlineKeyboardButton(
                text="7",
                callback_data=f"Yukki {ID7}|{duration7}|{user_id}",
            ),
            InlineKeyboardButton(
                text="8",
                callback_data=f"Yukki {ID8}|{duration8}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="9",
                callback_data=f"Yukki {ID9}|{duration9}|{user_id}",
            ),
            InlineKeyboardButton(
                text="10",
                callback_data=f"Yukki {ID10}|{duration10}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="««", callback_data=f"popat 2|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="🗑ᴄʟᴏsᴇ", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="»»", callback_data=f"popat 2|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def secondary_markup(videoid, user_id):
    buttons = [
        [ 
            InlineKeyboardButton(
                text="✨Uᴘᴅᴀᴛᴇs",
                url=f"https://t.me/insane_BOTS",
            ),
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ💫",
                url="https://t.me/x_d_nonsense",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴍᴏʀᴇ+", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close"),
        ],
    ]
    return buttons


def primary_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} »»»»» {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="ᴘᴀᴜsᴇ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"skipcb"),
        ],
        [
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ💫",
                url="https://t.me/insane_bots",
            ),
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close"),
        ],
    ]
    return buttons


def timer_markup(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} »»»»» {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="ᴘᴀᴜsᴇ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"skipcb"),
        ],
        [
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ💫",
                url="https://t.me/insane_bots",
            ),
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close"),
        ],
    ]
    return buttons


def audio_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} »»»»» {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="ᴘᴀᴜsᴇ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"skipcb"),
        ],
        [
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ💫",
                url="https://t.me/insane_bots",
            ),
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close"),
        ],
    ]
    return buttons


def audio_timer_markup_start(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} »»»»» {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="ᴘᴀᴜsᴇ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"skipcb"),
        ],
        [
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ💫",
                url="https://t.me/x_d_nonsense",
            ),
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close"),
        ],
    ]
    return buttons


audio_markup2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴘᴀᴜsᴇ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"skipcb"),
        ],
        [
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ💫",
                url="https://t.me/insane_bots",
            ),
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close"),
        ],
    ]
)

audio_markup201 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ʀᴇsᴜᴍᴇ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="ᴇɴᴅ", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ💫",
                url="https://t.me/insane_bots",
            ),
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close"),
        ],
    ]
)


audio_markup202 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ💫",
                url="https://t.me/insane_bots",
            ),
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close"),
        ],
    ]
)
