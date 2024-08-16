import random
import time as t
from discord.ext import commands


def HeadsOrTailsCommand(bot: commands.Bot):
    @bot.command()
    async def headsortails(ctx: commands.Context):
        pile_ou_face_list = ["Heads", "Tails"]
        the_answer = random.choice(pile_ou_face_list)
        t.sleep(0.7)
        await ctx.send(f"""**The coin landed on:**  ``{the_answer}``""")

    @bot.command()
    async def ht(ctx: commands.Context):
        await headsortails(ctx)