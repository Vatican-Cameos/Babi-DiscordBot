import discord
from discord.ext import commands

class BabiCog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whoareyou(self):
        """This does stuff!"""
        #Your code will go here
        await self.bot.say("Hi I am Babi. Nice to meet you.")

def setup(bot):
    bot.add_cog(BabiCog(bot))