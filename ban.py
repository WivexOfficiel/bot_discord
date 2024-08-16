import discord
from discord.ext import commands

def BanCommand(bot: commands.Bot):
    @bot.command(name='ban')
    async def ban(ctx: commands.Context, member: discord.Member, *, reason: str = ""):
        # Check if the command is being used in a private message
        if ctx.guild is None:
            return await ctx.send("You cannot use this command in a private message.")

        # Check if the user has permission to ban members
        if not ctx.author.guild_permissions.ban_members:
            return await ctx.send("You don't have permission to ban members.")

        # Check if the member can be banned (based on role hierarchy)
        if ctx.author.top_role <= member.top_role:
            return await ctx.send("You cannot ban this member.")

        # Provide a default reason if none is given
        if reason == "":
            reason = "No reason provided."

        # Ban the member and notify the channel
        await member.ban(reason=reason)
        return await ctx.send(f"{member.name} has been banned for: {reason}")

    @bot.command(name='b')
    async def b(ctx: commands.Context, member: discord.Member, *, reason: str = ""):
        # Check if the command is being used in a private message
        if ctx.guild is None:
            return await ctx.send("You cannot use this command in a private message.")

        # Check if the user has permission to ban members
        if not ctx.author.guild_permissions.ban_members:
            return await ctx.send("You don't have permission to ban members.")

        # Check if the member can be banned (based on role hierarchy)
        if ctx.author.top_role <= member.top_role:
            return await ctx.send("You cannot ban this member.")

        # Provide a default reason if none is given
        if reason == "":
            reason = "No reason provided."

        # Ban the member and notify the channel
        await member.ban(reason=reason)
        return await ctx.send(f"{member.name} has been banned for: {reason}")