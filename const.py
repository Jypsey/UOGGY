

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
            InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ', url='https://t.me/OGGYCINEEMAA_BOT?startgroup=true')           
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

HELP_MSG = """
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
- __If HyperLink, bot will return results in hyperlink format__
"""

ABOUT_MSG = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: <a href='https://t.me/OGGYCINEEMAA_BOT'>OGGY BOT</a>
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/BATMAN_CINEMAHUB'>Tʜɪs ᴘᴇʀsᴏɴ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://t.me/MYFASTSERVERR'>Qᴜɪᴄᴋ Fᴀsᴛ</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.0.3 [ Sᴛᴀʙʟᴇ ]</b>"""


REMOVE_WORDS = [
    "[MCU]", "@WMR", "Dramaost", "@R A R B G", "AMZN", "WEBDL", "WEB DL", "DVDRip", "HDRip", "HDTV", 
    "rarbg", "HSWEBDL", "10Bit", "WEBRip", "AAC", "DD5 1", "6CH", "2CH", "DDP5 1", "Mp3", "ESub", "EAC3", 
    "Uncut", "192Kbps", "HQ", "AVC", "UNTOUCHED", "mp4", "bluray", "@Ava", "384kbps", "192kbps", "WEB-DL", 
    "ZEE5", "10 bit", "10bit", "XVid", "unrated", "avc", "Hswebdl", "@MM LINKZ", "[MZM]", "@IM", "IMAX", 
    "EXTENDED", "viki", "iqiyi", "Seriesland4u", "DSNP", "DVDWO", "@MM OLD", "@CC", "Atmos", "Mubi", "AAC2 0", 
    "Repack", "proper", "Seriesland", "Mallu hub", "Mallumovies", "Mallumv", "Tamilmv", "Tamilrockers", "www", 
    "Directors cut", "FC_HEVC", "CDL", "Cdrama", "Kdrama", "Kdramaforyouall", "Ccineclub", "400MB", "250MB", 
    "500mB", "700MB", "900MB", "1600MB", "950MB", "600MB", "intermedia", "Sample", "CPTN5DW", "JrRip", "SH3LBY", 
    "Telly", "Primefix", "mkvCinemas", "HEvcbay", "Mkvking", "Dramahub", "Dramaday", "NF Webdl", "DDP5.1", 
    "Adrama Lovers", "TBPINDEX", "MZM", "MOVIEZ", "RAREFILMS", "Raremoviez", "backup", "Open matte", "AAC5.1 1", 
    "MCU", "YTS", "FULLHD", "HDSECTOR", "Extended", "vmax", "yessma", "king.com", "Divxtotal", "Tuktukcinema", 
    "Cimaclub.com", "Shahid4U.com", "Aflamfree", "backup", "DA Rips", "HDMovies", "kbps", "IMEDIASHARE", 
    "Rickychannel", "mubimovies", "CC ALL", "Infotainment", "mkvcage", "movie mania", "[Dno]", "zeemarathimovies", 
    "C C Channel", "WMR", "UCParadiso", "imovieshare", "Team HDT", "TeamHDT", "Toonsworld4all", "INTERNAL", "DnO", 
    "Cinemavilla", "Ongoing", "MMAX", "MM OLD", "[MM]", "Cinema naab", "NSSS", "[", "]", "mkv", "@MM", "Adrama", 
    "Toonworld4all", "SONYLIV", "SS DD 5 1", "DD 5 1", "CC Telugu", "Cc Tamil", "cc new", "hindimovies", "bm links", 
    "mm links", "Piro", "DS4K", "DDP5 1", "DDP 5 1", "voot", "Fanszz", "Tv2us", "CC ALL", "AAC2 0", "AAC", "(", ")", 
    "Ddp2 0", "FBM ALL", "FB TAMIL", "FBM HW", "FBM NEW", "FBM x265", "FBM KOREAN", "FBM", "KICKASS", "TORRENTS", 
    "@", "Dubbed", "Tamilblasters", "dubb", "ssrreq", "VGCINEMAS", "SNXT", "TG SKY MOVIES HD", "@R_A_R_B_G", "R_A_R_B_G",
    "@Team_KL", "MCArchives", "MwKLinks", "CK", "OTT", "PFM", "CC", "ᴍᴀ™", "CW", "TM LCM", "media", "🅰🆂🅺", "CL", "MLM",
    "ғαιвεяsgαтє", "SY MS", "MovieZmedia", "Team KL", "Tvserieshome", "MC", "CP", "www 1TamilMV one", "HEVC", "PFM", "TMCmovies offical",
    "TMC", "Telegram", "FC", "MM", "MS", "PM", "CK", "KC", "MG", "MOVIE", "CF", "CC", "Mj Linkz", "Moviesz", "Tamil LinkzZ", "MF"
]

STOP_WORDS = []
