from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("خطأ غير معروف!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("رد على الشخص ليتم كتمه!!.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("هذا المستخدم مكتوم بالفعل!!")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit(" تم سديت حلكة بعد ميحجي")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("خطأ غير معروف!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("رد على الشخص ليتم الغاء كتمه!!.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("هذا المستخدم غير مكتوم بالفعل!!")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("تم الغاء الكتم , فتحنا حلكك")

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?", allow_sudo=True)
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("خطأ غير معروف!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("رد على الشخص ليتم كتمه!!.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("هذا المستخدم مكتوم بالفعل!!")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("تم سديت حلكة بعد ميحجي")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?", allow_sudo=True)
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("خطأ غير معروف!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("رد على الشخص ليتم الغاء كتمه!!.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("هذا المستخدم غير مكتوم بالفعل!!")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("تم الغاء الكتم , فتحنا حلكك")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
