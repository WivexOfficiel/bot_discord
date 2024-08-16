import discord
from discord.ext import commands

commands.Bot.help_command = None

def HelpCommand(bot: commands.Bot):
    @bot.command(name='help')
    async def help(ctx):
        embed = discord.Embed(color=0x00ff01)

        # No Category
        embed.add_field(name="\n\n\n**┏—————— No Category ——————┓**\n\n",
                        value="`!help (h):` Shows this message\n\n"
                              "`!news (n):` Shows news updates\n\n",
                        inline=False)

        # Entertainment
        embed.add_field(name="\n\n\n**┏—————— Entertainment ——————┓**\n\n",
                        value="`!ping (p):` Responds with pong\n\n"
                              "`!randomnumber (rn) [amount]:` Generates a random number up to the specified amount\n\n"
                              "`!answer (a) [question]:` Answers your question(like a magic 8-ball)\n\n"
                              "`!headsortails (ht):` Flips a coin, landing on either heads or tails\n\n"
                              "`!story (s) [language]:` Tells a random story in the specified language (en, fr)\n\n",
                        inline=False)

        # Osint
        embed.add_field(name="\n\n\n**┏—————— OSINT ——————┓**\n\n",
                        value="`!serverinfo (si) [server invite]:` Shows information about a server\n\n"
                              "`!passwordcheck (pc) [password]:` Shows if a password leaked\n\n"
                              "`!socialsearch (ss) [username]:` Searches for a username across social media platforms\n\n",
                        inline=False)

        # Moderation
        embed.add_field(name="\n\n\n**┏—————— Moderation ——————┓**\n\n",
                        value="`!kick (k) [member] [reason]:` Kicks a member from the server with an optional reason\n\n"
                              "`!ban (b) [member] [reason]:` Bans a member from the server with an optional reason\n\n"
                              "`!clear (c) [amount]:` Clears an amount of messages from the chat\n\n"
                              "`!memberinfo (mi) [member]:` Shows member info\n\n",
                        inline=False)

        # Copy right
        embed.add_field(name='', value='\n\n\n© wivex', inline=True)

        # Send the embed message
        await ctx.send(embed=embed)

    @bot.command(name='h')
    async def h(ctx):
        await help(ctx)