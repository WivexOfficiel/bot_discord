import discord
import requests
from discord.ext import commands

client = discord.Client(intents=discord.Intents.default())

def SocialSearchCommand(bot: commands.Bot):
    @bot.command(name='socialsearch')
    async def socialsearch(ctx: commands.Context, *, username: str = ""):
            if username == "":
                await ctx.send("You have to put an username (use **!h** for more information)")

            else:
                platforms = ['twitter', 'instagram', 'facebook']
                results = []

                for platform in platforms:
                    url = f"https://{platform}.com/{username}"
                    response = requests.get(url)
                    if response.status_code == 200:
                        results.append(f"{platform.capitalize()} : {url}")
                    else:
                        results.append(f"{platform.capitalize()} : Non trouvé")

                await ctx.send('\n'.join(results))

    @bot.command()
    async def ss(ctx: commands.Context, *, username: str = ""):
        if username == "":
            await ctx.send("You have to put an username (use **!h** for more information)")

        else:
            platforms = ['twitter', 'instagram', 'facebook']
            results = []

            for platform in platforms:
                url = f"https://{platform}.com/{username}"
                response = requests.get(url)
                if response.status_code == 200:
                    results.append(f"{platform.capitalize()} : {url}")
                else:
                    results.append(f"{platform.capitalize()} : Non trouvé")

            await ctx.send('\n'.join(results))