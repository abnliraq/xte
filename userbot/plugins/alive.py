"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://t.me/x3raqe/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, التليثون شغال تاج راسي.  """
    await alive.edit("`Currently Alive, شلون الحجي!` **ψ(｀∇´)ψ**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     "`Bot Edited by:` [x3raqe](https://t.me//x3raqe), @x3raqe\n"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     "t.me/x3raqe")
