from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)
from pyrogram.enums import ParseMode, ChatMemberStatus
from pyrogram.errors import UserNotParticipant, QueryIdInvalid
from groupfilter import LOGGER, ADMINS
from groupfilter.db.fsub_sql import (
    add_fsub_req_user,
    is_req_user,
    add_fsub_reg_user,
    remove_fsub_users,
)
from groupfilter.db.settings_sql import get_admin_settings


async def check_fsub(
    bot, message, force_sub, link, request, user_id, file_id, admin_settings
):
    if isinstance(message, CallbackQuery):
        msg = message.message
    else:
        msg = message
        
    # If the user is an admin, skip the subscription check
    if user_id in ADMINS:
        return True
        
    if admin_settings:
        txt = admin_settings.fsub_msg or "**♦️ READ THIS INSTRUCTION ♦️\n\n🗣 നിങ്ങൾ ചോദിക്കുന്ന സിനിമകൾ നിങ്ങൾക്ക് ലഭിക്കണം എന്നുണ്ടെങ്കിൽ നിങ്ങൾ ഞങ്ങളുടെ ചാനലിലേക്ക് റിക്വസ്റ്റ് ചെയ്തിരിക്കണം. റിക്വസ്റ്റ് ചെയ്യാൻ  ⚓️ 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝘁𝗼 𝗝𝗼𝗶𝗻 ⚓️ എന്ന ബട്ടണിൽ അമർത്തിയാൽ നിങ്ങൾക്ക് ഞാൻ ആ സിനിമ അയച്ചു തരുന്നതാണ്..😍\n\n🗣 In Order To Get The Movie Requested By You in Our Group, You Must Have To join Our Official Channel First By Clicking ⚓️ 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗝𝗼𝗶𝗻 ⚓️ Button or the Link shown Below. I'll Send You That Movie 🙈\n\n👇CLICK ⚓️ 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗝𝗼𝗶𝗻 ⚓️👇**"
        fsub_img = getattr(admin_settings, "fsub_img", None)

    try:
        user = await bot.get_chat_member(int(force_sub), user_id)
        if user.status == ChatMemberStatus.BANNED:
            await msg.reply_text("Sorry, you are Banned to use me.", quote=True)
            return False
        return True

    except UserNotParticipant:
        try:
            user_det = await is_req_user(int(user_id), int(force_sub))
            if user_det and not user_det.fileid:
                return True

            if request:
                btn_txt = "⚓️ 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝘁𝗼 𝗝𝗼𝗶𝗻 ⚓️"
            else:
                btn_txt = "⚓ Join Channel"

            kb = InlineKeyboardMarkup([[InlineKeyboardButton(btn_txt, url=link)]])

            if admin_settings and admin_settings.fsub_msg and admin_settings.fsub_img:
                sub_msg = await msg.reply_photo(
                    photo=fsub_img,
                    caption=txt,
                    reply_markup=kb,
                    parse_mode=ParseMode.MARKDOWN,
                    quote=True,
                )
            elif admin_settings and admin_settings.fsub_msg:
                sub_msg = await msg.reply_text(
                    text=txt,
                    reply_markup=kb,
                    parse_mode=ParseMode.MARKDOWN,
                    quote=True,
                )
            else:
                sub_msg = await msg.reply_text(txt, reply_markup=kb, quote=True)

            try:
                if request:
                    await add_fsub_req_user(user_id, force_sub, file_id, sub_msg.id)
                else:
                    await add_fsub_reg_user(user_id, force_sub, file_id, sub_msg.id)
            except Exception as db_error:
                LOGGER.error(f"Database error in check_fsub: {db_error}")
                # Try to delete the message if DB operation failed
                try:
                    await sub_msg.delete()
                except:
                    pass
                return False

            return False

        except Exception as e:
            LOGGER.error(f"Error in UserNotParticipant handling: {e}")
            await msg.reply_text(
                text="Something went wrong, please try again later",
                quote=True,
            )
            return False

    except Exception as e:
        LOGGER.error(f"Unexpected error in check_fsub: {e}")
        await msg.reply_text(
            text="Something went wrong, please contact my support group",
            quote=True,
        )
        return False
    return True


async def check_inline_fsub(bot, query, force_sub, link, request, user_id, cnl):
    try:
        user = await bot.get_chat_member(int(force_sub), user_id)
        if user.status == ChatMemberStatus.BANNED:
            await query.answer(
                results=[],
                switch_pm_text="You are banned to use this bot",
                switch_pm_parameter="fs_bn",
                cache_time=1,
            )
            return False
    except UserNotParticipant:
        if request:
            user_det = await is_req_user(int(user_id), int(force_sub))
            if user_det:
                if not user_det.fileid:
                    return True
            inpt = "⚓ Tap Me to Request to Join channel."
            if int(cnl) == 1:
                sw_param = "fs_req_1"
            else:
                sw_param = "fs_req_2"
        else:
            inpt = "⚓ Tap Me to Join Channel"
            if int(cnl) == 1:
                sw_param = "fs_reg_1"
            else:
                sw_param = "fs_reg_2"

        try:
            await query.answer(
                results=[],
                cache_time=1,
                switch_pm_text=inpt,
                switch_pm_parameter=sw_param,
            )
            return False
        except QueryIdInvalid:
            pass
    except Exception as e:
        LOGGER.warning(e)
        await query.answer(
            results=[],
            switch_pm_text="Something went wrong, please contact my support group",
            switch_pm_parameter="fs_er",
            cache_time=1,
        )
        return False
    return True


@Client.on_message(filters.command(["clearfsubusers"]) & filters.user(ADMINS))
async def log_file(bot, message):
    rem = await remove_fsub_users()
    if rem:
        await message.reply_text("All fsub users removed from database")
    else:
        await message.reply_text("No fsub users found in database")


async def get_inline_fsub(bot, update):
    if isinstance(update, CallbackQuery):
        msg = update.message
    elif isinstance(update, Message):
        msg = update

    try:
        await msg.delete()
    except Exception as e:
        LOGGER.warning(e)

    user_id = update.from_user.id
    cmd = update.command[1]
    mode = cmd.split("_")[1]
    if mode.startswith("re"):
        cnl = cmd.split("_")[2]

        admin_settings = await get_admin_settings()
        if admin_settings:
            request = admin_settings.join_req

            if admin_settings.fsub_msg:
                fsub_msg = admin_settings.fsub_msg
                txt = fsub_msg
            else:
                txt = "**Please join below channel to use me inline!**"
            if admin_settings.fsub_img:
                fsub_img = admin_settings.fsub_img
            else:
                fsub_img = None

            if int(cnl) == 1:
                force_sub = admin_settings.fsub_channel
                link = admin_settings.channel_link
            else:
                force_sub = admin_settings.fsub_channel2
                link = admin_settings.channel_link2

            if mode == "req":
                btn_txt = "⚓ Request to Join channel to use me inline."
            else:
                btn_txt = "⚓ Join Channel to use me inline."

            kb = InlineKeyboardMarkup([[InlineKeyboardButton(btn_txt, url=link)]])

            if admin_settings and admin_settings.fsub_msg and admin_settings.fsub_img:
                sub_msg = await msg.reply_photo(
                    photo=fsub_img,
                    caption=txt,
                    reply_markup=kb,
                    parse_mode=ParseMode.MARKDOWN,
                    quote=True,
                )
            elif admin_settings and admin_settings.fsub_msg:
                sub_msg = await msg.reply_text(
                    text=txt,
                    reply_markup=kb,
                    parse_mode=ParseMode.MARKDOWN,
                    quote=True,
                )
            else:
                sub_msg = await msg.reply_text(txt, reply_markup=kb, quote=True)

            if request:
                await add_fsub_req_user(
                    user_id, force_sub, fileid="fsub", msg_id=sub_msg.id
                )
            else:
                await add_fsub_reg_user(
                    user_id, force_sub, fileid="fsub", msg_id=sub_msg.id
                )
    elif mode.startswith("bn"):
        await msg.reply_text("You are banned to use this bot", quote=True)
        return
    elif mode.startswith("er"):
        await msg.reply_text(
            "Something went wrong, please contact my support group", quote=True
        )
        return
