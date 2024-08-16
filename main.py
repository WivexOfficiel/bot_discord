"""
Script by: wivex
Version: 1.0
"""


import discord
from discord.ext import commands
import asyncio

### Import uncategorized package
from scripts_global.commands.uncategorized.help import HelpCommand
from scripts_global.commands.uncategorized.news import NewsCommand

### Import entertainment packages
from scripts_global.commands.entertaiment.answer import AnswerCommand
from scripts_global.commands.entertaiment.heads_or_tails import HeadsOrTailsCommand
from scripts_global.commands.entertaiment.ping import PingCommand
from scripts_global.commands.entertaiment.random_number import RandomNumberCommand
from scripts_global.commands.entertaiment.story import StoryCommand

### Import moderation packages
from scripts_global.commands.moderation.ban import BanCommand
from scripts_global.commands.moderation.clear import ClearCommand
from scripts_global.commands.moderation.kick import KickCommand
from scripts_global.commands.moderation.memberinfo import MemberInfoCommand

### Import osint packages
from scripts_global.commands.osint.password_check import PasswordCheckCommand
from scripts_global.commands.osint.server_info import ServerInfoCommand
from scripts_global.commands.osint.socialsearch import SocialSearchCommand

### Import events packages
from scripts_global.events.events import setup_events


### Configuration des tokens des bots
BOT_TOKEN_COLT = ''


### Créer les deux instances de bots
bot_colt = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot_c3po= commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot_r2d2 = commands.Bot(command_prefix='!', intents=discord.Intents.all())


### Charger les commandes et événements pour les deux bots
def load_commands(bot):
    # Uncategorized
    HelpCommand(bot)
    NewsCommand(bot)

    # Entertaiment
    AnswerCommand(bot)
    HeadsOrTailsCommand(bot)
    PingCommand(bot)
    RandomNumberCommand(bot)
    StoryCommand(bot)

    # Moderation
    BanCommand(bot)
    ClearCommand(bot)
    KickCommand(bot)
    MemberInfoCommand(bot)

    # Osint
    ServerInfoCommand(bot)
    PasswordCheckCommand(bot)
    SocialSearchCommand(bot)

    # Events
    setup_events(bot)


bot_intents_list = [bot_colt, bot_c3po, bot_r2d2]


for bot in bot_intents_list:
    load_commands(bot)

### Fonction pour lancer les bots simultanément
async def start_bots():
    await asyncio.gather(
        bot_colt.start(BOT_TOKEN_COLT),
        bot_c3po.start(BOT_TOKEN_C3PO),
        bot_r2d2.start(BOT_TOKEN_R2D2),
                         )

if __name__ == "__main__":
    asyncio.run(start_bots())