import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

from util.auto_cog_loader import load_cog_files
from util import load_teams

DOTENV_PATH = '../hidden.env'

load_dotenv(DOTENV_PATH)
BOT_TOKEN = os.environ.get('TOKEN')

intents = discord.Intents().all()
permissions = discord.Permissions.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)

teams = load_teams.init("../assets/MPCL_S10_Div1.csv")


@bot.event
async def on_ready():
    print("Engineer ready")


def run_discord_bot():
    cog_dir = ["./cogs"]
    load_cog_files(bot, cog_dir)
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    run_discord_bot()
