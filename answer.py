import random
import time as t
from discord.ext import commands

def AnswerCommand(bot: commands.Bot):
    @bot.command()
    async def answer(ctx: commands.Context, *, question: str = ""):
        if question == "":
            await ctx.send("You have to put a question (use **!h** for more information)")

        else:
            positive_answer_list = ["Yes", "Certainly", "100%"]
            negative_answer_list = ["No", "Certainly not", "Never"]
            unknown_answer_list = ["I don't know", "Maybe", "You must try again", "Impossible for me to answer"]
            combined_list = positive_answer_list + negative_answer_list + unknown_answer_list
            the_answer = random.choice(combined_list)
            t.sleep(1)
            await ctx.send(f"""
**The answer to your question:**
_{question}_
    
**Is:**
_{the_answer}_""")

    @bot.command(name='a')
    async def a(ctx: commands.Context, *, question: str):
        if question == "":
            await ctx.send("You have to put a question (use **!h** for more information)")

        else:
            positive_answer_list = ["Yes", "Certainly", "100%"]
            negative_answer_list = ["No", "Certainly not", "Never"]
            unknown_answer_list = ["I don't know", "Maybe", "You must try again", "Impossible for me to answer"]
            combined_list = positive_answer_list + negative_answer_list + unknown_answer_list
            the_answer = random.choice(combined_list)
            t.sleep(1)
            await ctx.send(f"""
**The answer to your question:**
_{question}_

**Is:**
_{the_answer}_""")