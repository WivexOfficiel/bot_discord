import discord
from discord.ext import commands


def NewsCommand(bot: commands.Bot):
    @bot.command(name='news')
    async def news(ctx: commands.Context):
        embed = discord.Embed(color=0x00bbff)

        # Title
        embed.add_field(name="             **NEWS**", value="", inline=False)

        # No Category
        embed.add_field(name="\n\n\n**┏—————— No Category ——————┓**\n\n",
                        value="_nothing..._",
                        inline=False)

        # Entertainment
        embed.add_field(name="\n\n\n**┏—————— Entertainment ——————┓**\n\n",
                        value="`!answer (a) [question]:` _Answers your question(like a magic 8-ball)_\n\n"
                              "`!headsortails (ht):` _Flips a coin, landing on either heads or tails_\n\n"
                              "`!story (s) [language]:` _Tells a random story in the specified language (en, fr)_\n\n",
                        inline=False)

        # Osint
        embed.add_field(name="\n\n\n**┏—————— OSINT ——————┓**\n\n",
                        value="`!passwordcheck (p) [password]:` _Shows if a password has leaked_\n\n"
                              "`!socialsearch (ss) [username]:` _Searches for a username across social media platforms_\n\n",
                        inline=False)

        # Moderation
        embed.add_field(name="\n\n\n**┏—————— Moderation ——————┓**\n\n",
                        value="`!memberinfo (mi) [member]:` Shows member info\n\n",
                        inline=False)

        # Copy right
        embed.add_field(name='', value='\n\n\n© wivex', inline=True)

        # Send the embed message
        await ctx.send(embed=embed)

    @bot.command(name='n')
    async def n(ctx: commands.Context):
        await news(ctx)