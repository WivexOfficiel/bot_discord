import discord
from discord.ext import commands

def ClearCommand(bot: commands.Bot):
    @bot.command(name='clear')
    async def clear(ctx: commands.Context, amount: int = 5) -> discord.Message:
        print(f"Clear command executed with amount = {amount}")

        # Check if the command is being used in a private message
        if ctx.guild is None:
            return await ctx.send("You cannot use this command in a private message.")

        # Check if the user has permission to manage messages
        if not ctx.author.guild_permissions.manage_messages:
            return await ctx.send("Only moderators can use this command.")

        # Check if the amount exceeds the limit of 100 messages
        if amount > 100:
            return await ctx.send("The maximum number of messages that can be deleted is 100.")

        # Ensure the command is being run in a text channel
        if not isinstance(ctx.channel, discord.TextChannel):
            return await ctx.send("You must run this command in a text channel.")

        # Purge the specified number of messages plus the command message itself
        await ctx.channel.purge(limit=amount + 1)

        if amount == 1:
            return await ctx.send(f"{amount} message deleted.")
        else:
            return await ctx.send(f"{amount} messages deleted.")

    @bot.command(name='c')
    async def c(ctx: commands.Context, amount: int = 5) -> discord.Message:
        await clear(ctx, amount)