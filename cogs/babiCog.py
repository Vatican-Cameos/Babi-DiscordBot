import discord
from discord.ext import commands
import random
babiRespondsList = ["What?", "What do you want?" ,"yes?" , "Who called me?", "What did you say?"]
class BabiCog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whoareyou(self):
        """This does stuff!"""
        #Your code will go here
        await self.bot.say("Hi I am Babi. Nice to meet you.")

    @commands.command()
    async def watevs(self):
        """¯\_(ツ)_/¯"""
        #Code
        await self.bot.say("¯\_(ツ)_/¯")

    @commands.command()
    async def ty(self,user : discord.Member):
        """Thanks a friend"""
        await self.bot.say("Why thank you, " + user.mention)

    @commands.command()
    async def add (self,a : int ,b : int):
        """I'm a mathematician let me add you some numbers"""
        x = a+b;
        await self.bot.say("Well after hours of computation I think the sum is " + str(x))
    
    @commands.command()
    async def whoisawesome (self):
        """Analyzes the behavior of each user and a uses a complex algorithm which mentions the coolest person of the group"""
       	
        await self.bot.say(":point_up_2::skin-tone-3: ")


    async def check_listener(self, message):
        botUserMention = (self.bot.user.mention)
        botUser  = (self.bot.user.name)

        greetingsList = ["Hi kind sir", "How you doing? " ,"What's up "+ message.author.name, "Hey! "+ message.author.name, "Hola, good day kind sir. " , "Enappa rajkumar ? oota ayta"]
        byeList = ["Bye", "See you", "Take care", "Good night"]
        if message.content.startswith("hi"):
            await self.bot.send_message(message.channel , random.choice(greetingsList))
        elif ( botUser in message.content or  str(botUserMention) in message.content or botUser.lower() in message.content or message.content.startswith(botUser)):
            await self.bot.send_message(message.channel, random.choice(babiRespondsList))
        elif message.content.startswitch("bye"):
        	await self.bot.send_message(message.channel , random.choice(byeList))    

def setup(bot):
    n = BabiCog(bot)
    bot.add_listener(n.check_listener, "on_message")
    bot.add_cog(n)
