from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("حزين ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("😊")
        await asyncio.sleep(3.5)
        await event.edit("🙂")
        await asyncio.sleep(4.1)
        await event.edit("🙁")
        await asyncio.sleep(3.5)
        await event.edit("☹️")
        await asyncio.sleep(2.2)
        await event.edit("❤️")
        await asyncio.sleep(3.1)
        await event.edit("💔")
