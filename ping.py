from discord.ext import commands

def PingCommand(bot: commands.Bot):
    @bot.command()
    async def ping(ctx: commands.Context):
        await ctx.send("pong")

    @bot.command()
    async def p(ctx: commands.Context):
        await ping(ctx)