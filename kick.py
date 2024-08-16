import discord
from discord.ext import commands

def KickCommand(bot: commands.Bot):
    @bot.command(name='kick')
    async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = ""):
        is_in_private_message = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_message:
            return await ctx.send("You cannot use this command in a private message.")

        has_permission = ctx.author.guild_permissions.kick_members
        if not has_permission:
            return await ctx.send("Only moderators can use this command.")

        is_kickable = ctx.author.top_role > member.top_role
        if not is_kickable:
            return await ctx.send("You cannot kick this member.")

        if reason == "":
            reason = "no reason provided"

        await member.kick(reason=reason)
        return await ctx.send(f"{member.name} has been kicked for {reason}")

    @bot.command(name='k')
    async def k(ctx: commands.Context, member: discord.Member, *, reason: str = ""):
        is_in_private_message = ctx.guild is None and isinstance(ctx.author, discord.User)
        if is_in_private_message:
            return await ctx.send("You cannot use this command in a private message.")

        has_permission = ctx.author.guild_permissions.kick_members
        if not has_permission:
            return await ctx.send("Only moderators can use this command.")

        is_kickable = ctx.author.top_role > member.top_role
        if not is_kickable:
            return await ctx.send("You cannot kick this member.")

        if reason == "":
            reason = "no reason provided"

        await member.kick(reason=reason)
        return await ctx.send(f"{member.name} has been kicked for {reason}")