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

    animation_interval = 0.1

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "كيوت":

        await event.edit(input_str)

        animation_chars = [

            "🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️♥️♥️♥️♥️\n🥺🥺🥺🥺🥺",
            "♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️♥️♥️♥️♥️",    
            "🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n♥️🥺♥️🥺♥️",
            "♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n🥺♥️🥺♥️🥺",
            "🥺♥️🥺♥️🥺\n♥️♥️♥️♥️♥️\n🥺♥️🥺♥️🥺\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️",
            "♥️🥺♥️🥺♥️\n♥️🥺♥️🥺♥️\n♥️🥺♥️🥺♥️\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺",
            "🥺♥️🥺♥️🥺\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️",
            "♥️🥺♥️🥺♥️\n🥺🥺🥺🥺🥺\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺"
                        "🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️♥️♥️♥️♥️\n🥺🥺🥺🥺🥺",
            "♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️♥️♥️♥️♥️",    
            "🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n♥️🥺♥️🥺♥️",
            "♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n🥺♥️🥺♥️🥺",
            "🥺♥️🥺♥️🥺\n♥️♥️♥️♥️♥️\n🥺♥️🥺♥️🥺\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️",
            "♥️🥺♥️🥺♥️\n♥️🥺♥️🥺♥️\n♥️🥺♥️🥺♥️\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺",
            "🥺♥️🥺♥️🥺\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️",
            "♥️🥺♥️🥺♥️\n🥺🥺🥺🥺🥺\n🥺♥️🥺♥️🥺\n♥️🥺♥️🥺♥️\n🥺♥️🥺♥️🥺"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 8])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 117)

    input_str = event.pattern_match.group(1)

    if input_str == "احبج":

        await event.edit(input_str)

        animation_chars = [

            "أحـٰٚبـ̷ِْــٰۛچ",
            "🤤♥️",    
            "موت عليج",
            "@x3raqe",
            "تعي خاص",
            "🥺🎈",
            "تعي نزوج",
            "😭🥺",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])