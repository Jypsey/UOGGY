from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_KB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🔗 ᴏᴜʀ ᴄʜᴀɴᴇʟꜱ ʟɪɴᴋꜱ 🔗', url='https://t.me/CINEMAHUB_LINK')
            ],[
            InlineKeyboardButton('📌 ᴍʏ ɢʀᴏᴜᴘ', url='https://t.me/+rotT30StVG1hYmZl'),
            InlineKeyboardButton('🛠 ᴍʏ ᴏᴡɴᴇʀ', url='https://t.me/BATMAN_CINEMAHUB')
            ],[
            InlineKeyboardButton('⚠️ ʜᴇʟᴘ', callback_data='help_cb'),
            InlineKeyboardButton('⚙️ ᴀʙᴏᴜᴛ', callback_data='about_cb')
            ],[
            InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ', url='https://t.me/OGGYCINEMAA_BOT?startgroup=true')           
        ]
    ]
)
HELP_KB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙 Back", callback_data="back_m"),
        ],
    ]
)


START_MSG ="""Hi <b><a href='tg://user?id={user_id}'>{name}</a></b>,  
ഞാൻ ഒരു <b>AUTO FILTER BOT</b> ആണ്, എന്റെ ഉടമസ്ഥർ <a href='https://t.me/+sZr3rX7Al48yZTI1'>CINEMA-HUB</a> ആണ്, നിങ്ങൾക്കും നിങ്ങളുടെ ഗ്രൂപ്പുകളിൽ ഇപ്പോൾ എന്നെ ഉപയോഗിക്കാവുന്നതാണ്"""


HELPMSG = """
**You can find the bot commands here.**
**Group Commands:-**
/help - __Show this help message__
/settings - __Toggle settings of Precise Mode and Button Mode__
`Precise Mode:` 
- __If Enabled, bot will match the word & return results with only the exact match__
- __If Disabled, bot will match the word & return all the results containing the word__ 
`Result Mode:` 
- __If Button, bot will return results in button format__
- __If List, bot will return results in list format__
- __If HyperLink, bot will return results in hyperlink format__

**Admin Commands:-**
/logs - __Get logs as a file__
/server - __Get server stats__
/restart - __Restart the bot__
/stats - __Get bot user stats__
/broadcast - __Reply to a message to send that to all bot users__
/index - __Start indexing a database channel (bot must be admin of the channel if that is provate channel)__
__You can just forward the message from database channel for starting indexing, no need to use the /index command__
/delete - __Reply to a file to delete it from database__
/autodelete - __Set file auto delete time in seconds__
/repairmode - __Enable or disable repair mode - If on, bot will not send any files__
/customcaption - __Set custom caption for files__
/adminsettings - __Get current admin settings__
/ban - __Ban a user from bot__ - `/ban user_id`
/unban - __Unban a user from bot__ - `/unban user_id`
/addfilter - __Add a text filter__ - `/addfilter filter message` __or__ `/addfilter "filter multiple words" message` __(If a filter is there, bot will send the filter rather than file)__
/delfilter - __Delete a text filter__ - `/delfilter filter`
/listfilters - __List all filters currently added in the bot__
/forcesub - __Set force subscribe channel__ - `/forcesub channel_id` __Bot must be admin of that channel (Bot will create a new invite link for that channel)__
/checklink - __Check invite link for force subscribe channel__
/total - __Get count of total files in DB__
"""

SET_MSG = """
**Below are your current settings:**
`Info`
**Precise Mode:** 
- __If Enabled, bot will match the word & return results with only the exact match__
- __If Disabled, bot will match the word & return all the results containing the word__    
**Result Mode:**
- __If HyperLink, bot will return results in hyperlink format__
- __If Button, bot will return results in button format__
- __If List, bot will return results in list format__


__You can toggle with right side buttons__:-"""


ABOUT_MSG = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: <a href='https://t.me/OGGYCINEMAA_BOT'>OGGY BOT</a>
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/BATMAN_CINEMAHUB'>Tʜɪs ᴘᴇʀsᴏɴ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://t.me/MYFASTSERVERR'>Qᴜɪᴄᴋ Fᴀsᴛ</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.0.3 [ Sᴛᴀʙʟᴇ ]</b>"""

ST_HELP_MSG = """
**You can find the bot commands here.**
**Group Commands:-**
‣/help - __Show this help message__
‣/settings - __Toggle settings of Precise Mode and Button Mode__
`Precise Mode:` 
- __If Enabled, bot will match the word & return results with only the exact match__
- __If Disabled, bot will match the word & return all the results containing the word__ 
`Result Mode:` 
- __If Button, bot will return results in button format__
- __If List, bot will return results in list format__
- __If HyperLink, bot will return results in hyperlink format__"""

