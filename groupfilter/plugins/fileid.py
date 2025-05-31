from pyrogram import *

@Client.on_message(filters.command("getfileid"))
async def getfileid(c, m):
    if m.reply_to_message.document:
        await m.reply(f"Here is {m.reply_to_message.document.file_id}")
    elif m.reply_to_message.video:
        await m.reply(f"Here is {m.reply_to_message.video.file_id}")
    else:
        await m.reply("Reply to a video or file")
