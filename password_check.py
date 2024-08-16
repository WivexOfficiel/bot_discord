import discord
import hashlib
import requests
from discord.ext import commands

client = discord.Client(intents=discord.Intents.default())

def PasswordCheckCommand(bot: commands.Bot):
    @bot.command(name='passwordcheck')
    async def passwordcheck(ctx: commands.Context, *, password: str = ""):
        if password == "":
            await ctx.send("You have to put a password (use **!h** for more information)")

        else:
            sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
            prefix = sha1_password[:5]
            suffix = sha1_password[5:]
            response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')

            if suffix in response.text:
                await ctx.send("⚠ This password has been compromised.")
            else:
                await ctx.channel.send("✅ This password was not found in any breaches.")

    @bot.command(name='pc')
    async def pc(ctx: commands.Context, *, password: str = ""):
        if password == "":
            await ctx.send("You have to put a password (use **!h** for more information)")

        else:
            sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
            prefix = sha1_password[:5]
            suffix = sha1_password[5:]
            response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')

            if suffix in response.text:
                await ctx.send("⚠ This password has been compromised.")
            else:
                await ctx.channel.send("✅ This password was not found in any breaches.")