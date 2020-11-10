"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""
from telethon import events
import asyncio


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "x3raqe":
        await event.edit(input_str)
        animation_chars = [
            "اني",
            "محمد نزار الدليمي",
            "19 سنة",
            "من المريخ",
            "☹️🖤"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])
