import discord
from discord.ext import commands

def setup_events(bot: commands.Bot):
    @bot.event
    async def on_ready():
        print("Bot is connect to discord  |  Bot name: ", bot.user.name, "  |  Bot ID: ", bot.user.id)

    @bot.event
    async def on_message(message: discord.Message):
        if 'xorjar' in message.content:
            await message.channel.send("c du reel")
        if 'vivex' in message.content:
            await message.channel.send("Tg")
        if 'louis' in message.content:
            await message.channel.send("Tu pu")
        await bot.process_commands(message)