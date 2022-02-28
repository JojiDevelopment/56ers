# Standard
import discord
from discord.commands import slash_command, Option
from discord.ext import commands, tasks
from datetime import time, datetime

# Local
from utils.api import ValorantAPI

#valorant_api
#available regions: eu, ap, na, kr | (latem, br = 'na')

#slash_server_id

class valorant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
         
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'-{self.__class__.__name__}')
    
    @slash_command(description="Shows my daily store")
    async def store(self, interaction, region: Option(str, "Region (eu, ap, na, kr)"), username: Option(str, "Input username"), password: Option(str, "Input password")):
        api = ValorantAPI(interaction, username, password, region)
        await api.start()
        
def setup(bot):
    bot.add_cog(valorant(bot))