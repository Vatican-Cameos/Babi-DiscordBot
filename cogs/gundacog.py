import discord
from discord.ext import commands
from random import choice as randchoice

class Gundacog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!!!")

    @commands.command(pass_context = True)
    async def myname(self,ctx):
        """Gives your username"""

        #Your code will go here
        user = ctx.message.author
        await self.bot.say(user.display_name)

    @commands.command(pass_context = True)
    async def pick(self,ctx):
        """Picks a random user from the channel who are online"""

        #Your code will go here
        server = ctx.message.server
        people = []
        for x in server.members:
            if x.status == discord.Status.online:
                people.append(x)
        await self.bot.say(randchoice(people))

def setup(bot):
    bot.add_cog(Gundacog(bot))