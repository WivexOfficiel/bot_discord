import random
from discord.ext import commands


def StoryCommand(bot: commands.Bot):
    @bot.command()
    async def story(ctx: commands.Context, *, language_user: str = ""):
        def read_file_content(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

        language = None

        if language_user == "":
            await ctx.send("You have to choose a language (use **!h** for more information)")
            return

        language_user = language_user.upper()
        if language_user in ['FR', 'FRANCAIS', 'FRANÇAIS', 'FRANCAISE', 'FRANÇAISE', 'FRENCH']:
            language = 'fr'
            story_name_list = ['la_foret_enchantee.txt', 'le_voyage_dans_le_temps.txt', 'le_chat_et_la_lune.txt']

        elif language_user in ['EN', 'ENGLISH', 'ANGLAIS']:
            language = 'en'
            story_name_list = ['the_enchanted_forest.txt', 'the_time_travel.txt', 'the_cat_and_the_moon.txt']

        if language:

            the_story = random.choice(story_name_list)

            the_story_directory = f"scripts/commands/entertaiment/stories/{language}/{the_story}"

            try:
                content_file = read_file_content(the_story_directory)
                await ctx.send(content_file)

            except FileNotFoundError:
                await ctx.send(f"Sorry, the story file {the_story_directory} was not found.")

            except Exception as e:
                await ctx.send(f"An error occurred: {e}")

        else:
            await ctx.send("Language not recognized. Please use **!h** for help.")

    @bot.command(name='s')
    async def s(ctx: commands.Context, *, language_user: str = ""):
        def read_file_content(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

        language = None

        if language_user == "":
            await ctx.send("You have to choose a language (use **!h** for more information)")
            return

        language_user = language_user.upper()
        if language_user in ['FR', 'FRANCAIS', 'FRANÇAIS', 'FRANCAISE', 'FRANÇAISE', 'FRENCH']:
            language = 'fr'
            story_name_list = ['la_foret_enchantee.txt', 'le_voyage_dans_le_temps.txt', 'le_chat_et_la_lune.txt']

        elif language_user in ['EN', 'ENGLISH', 'ANGLAIS']:
            language = 'en'
            story_name_list = ['the_enchanted_forest.txt', 'the_time_travel.txt', 'the_cat_and_the_moon.txt']

        if language:

            the_story = random.choice(story_name_list)

            the_story_directory = f"scripts/commands/entertaiment/stories/{language}/{the_story}"

            try:
                content_file = read_file_content(the_story_directory)
                await ctx.send(content_file)

            except FileNotFoundError:
                await ctx.send(f"Sorry, the story file {the_story_directory} was not found.")

            except Exception as e:
                await ctx.send(f"An error occurred: {e}")

        else:
            await ctx.send("Language not recognized. Please use **!h** for help.")