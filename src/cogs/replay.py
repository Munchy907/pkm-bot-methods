import discord
import requests

from discord import option
from discord.ext import commands
from discord.commands.context import ApplicationContext
from main import teams


class ReplayHandler(commands.Cog):

    @discord.slash_command(description="Takes the replay link and outputs a formatted version of it to include the teams that played")
    async def save_replay(self, ctx: ApplicationContext, url: str):
        if url.startswith("https://replay.pokemonshowdown.com/") is False and url.startswith(
                "http://replay.pokemonshowdown.com/") is False:
            await ctx.respond("Error: Invalid link! Please provide links from showdown only")
            return

        team1 = []
        team2 = []

        response = requests.get(url + ".log", stream=True)
        for line in response.iter_lines():
            if isinstance(line, bytes):
                line = line.decode('utf-8')

            if line.startswith("|poke|p1|"):
                end_pos = line.rfind('|')
                if line.find(',') != -1:
                    end_pos = line.find(',')
                team1.append(line[line.index("p1|") + 3:end_pos])
            elif line.startswith("|poke|p2|"):
                end_pos = line.rfind('|')
                if line.find(',') != -1:
                    end_pos = line.find(',')
                team2.append(line[line.index("p2|") + 3:end_pos])

        coach1 = teams.get_coach(team1)
        coach2 = teams.get_coach(team2)

        await ctx.send(f"{coach1} vs {coach2} \n {url}")


def setup(bot):  # this is called by Pycord to set up the cog
    bot.add_cog(ReplayHandler(bot))  # add the cog to the bot
