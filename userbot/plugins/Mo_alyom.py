from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("مو ليوم?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("مو ليوم")
        await asyncio.sleep(0.5)
        await event.edit("باجر")
        await asyncio.sleep(0.6)
        await event.edit("عكب باجر")
        await asyncio.sleep(0.5)
        await event.edit("شهر")
        await asyncio.sleep(0.6)
        await event.edit("سنه")
        await asyncio.sleep(0.5)
        await event.edit("واطب ليجوه امرع دينك")