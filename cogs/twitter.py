import discord
from discord.ext import commands
from twython import Twython

APP_KEY = 'QJgiEZhENKSTzDNDeTfTsI2AE'  # Customer Key here
APP_SECRET = 'XEkTsRe2g4dvbjAIU5wmZELNCMjnUjBmLBdzLnqkAKMtZbxdjY'  # Customer secret here
OAUTH_TOKEN = '805365609475121152-8mgaamluTxKUmzf64ACiDQXbbdBK3wp'  # Access Token here
OAUTH_TOKEN_SECRET = 'K457wpwQ32oALZzAr3uZpQsbOQN4HxFXkr9nbi8LvInKG'  # Access Token Secret here

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)    
    async def tweet(self,ctx,message):
        """This does stuff!"""
        #Your code will go here
        msg  = ctx.message.content
        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        twitter.update_status(status=message)
        await self.bot.say("Babi tweeted this : " + message)

def setup(bot):
    bot.add_cog(Mycog(bot))
