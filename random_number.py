import random
from discord.ext import commands

def RandomNumberCommand(bot: commands.Bot):
    @bot.command(name='randomnumber')
    async def randomnumber(ctx: commands.Context, *, number: int = None):
        if not number:
            await ctx.send("You have to put an amount (use **!h** for more information)")

        else:
            the_number = random.randint(1, number)
            await ctx.send(f"The chosen number is: **{the_number}**")

    @bot.command(name='rn')
    async def rn(ctx: commands.Context, *, number: int = None):
        if not number:
            await ctx.send("You have to put an amount (use **!h** for more information)")

        else:
            the_number = random.randint(1, number)
            await ctx.send(f"The chosen number is: **{the_number}**")