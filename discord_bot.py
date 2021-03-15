import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import discord_bot_info
import db
import requests
import urllib

skarr = Bot(command_prefix="!")

@skarr.event
async def on_message(message):
    await skarr.process_commands(message)
    mention = f'<@!{skarr.user.id}>'

    quote = db.get_random_quote()

    if mention in message.content:
        await message.channel.send(quote[1])

@skarr.command()
async def quote(message, *args):
    channel = message.channel

    quote = args[:]

    separator = ' '
    joined_quote = separator.join(quote)

    db.add_quote_to_db(joined_quote)

skarr.run(discord_bot_info.BOT_TOKEN)