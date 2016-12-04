import discord
from discord.ext import commands
#bot = commands.Bot(command_prefix='!')

class ZeroCog:
    """My custom cog that does stuff!"""
    def __init__(self,bot,message):
        self.bot = bot
        self.bot.send_message(message.channel,"HELLO!")
    
    @commands.command()
    async def firstcom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")
        self.bot.send_message(message.channel,"HELLO!")

    @commands.command(pass_context=True)
    async def all(self, ctx):
        server = ctx.message.server
        for user in server.members:
            await self.bot.say("Hi "+str(user) )
    
def setup(bot):
    bot.add_cog(ZeroCog(bot))