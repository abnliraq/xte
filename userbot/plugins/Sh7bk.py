from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("شحبك?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("🥺احبك🖤")
        await asyncio.sleep(0.5)
        await event.edit("🥺اعشكك🖤")
        await asyncio.sleep(0.6)
        await event.edit("🖤اموت بيك🥺")
        await asyncio.sleep(0.5)
        await event.edit("🖤فديتك🥺")
        await asyncio.sleep(0.6)
        await event.edit("🖤يكيوت🥺")
        await asyncio.sleep(0.5)
        await event.edit("♥️يقلبي🥺")
        await asyncio.sleep(0.6)
        await event.edit("♥️حياتي🥺")
        await asyncio.sleep(0.5)
        await event.edit("😭♥️")