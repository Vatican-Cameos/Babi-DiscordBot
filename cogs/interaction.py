import discord
from discord.ext import commands
from .utils.dataIO import dataIO
import random

babiRespondsList = ["What?", "What do you want?" ,"yes?" , "Who called me?", "What did you say?"]
channel_id = '252375277076873216'
channel = discord.Object(channel_id)

class BabiCog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        #self.file_path = "data/user/channel.json"
        #self.channel_default = dataIO.load_json(self.file_path)

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
    
    @commands.command(pass_context=True)
    async def whoisonline(self,ctx):
        """Returns members who are online"""

        server = ctx.message.server
        for member in server.members:
            if member.status == discord.Status.online or member.status == discord.Status.idle:
                await self.bot.say(member)

    @commands.command(pass_context = True)
    async def register_channel(self, ctx):
        """Registers a channel into your local system, which is going to be your default channel"""
        #del c.channel_default["id"]
        #channel_id = msg 
        #c.channel_default["id"] = ctx.message.channel
        #dataIO.save_json(self.file_path,self.channel_default)

    async def on_message_listener(self, message):
        botUserMention = (self.bot.user.mention)
        botUser  = (self.bot.user.name)

        greetingsList = ["Hi kind sir", "How you doing? " ,"What's up "+ message.author.name, "Hey! "+ message.author.name, "Hola, good day kind sir. " , "Enappa rajkumar ? oota ayta"]
        byeList = ["Bye", "See you", "Take care", "Good night"]
        if botUser != message.author.name:
            if message.content.startswith("hi"):
                await self.bot.send_message(message.channel , random.choice(greetingsList))
            elif ( botUser in message.content or  str(botUserMention) in message.content or botUser.lower() in message.content or botUser.upper() in message.content or message.content.startswith(botUser)):
                await self.bot.send_message(message.channel, random.choice(babiRespondsList))
            elif message.content.startswith("bye"):
                await self.bot.send_message(message.channel , random.choice(byeList)) 

    async def on_member_update_listener(self, before_member, after_member):
        old_status = before_member.status
        new_status = after_member.status
        if(str(old_status) == "idle"):
            if(str(new_status) == "online"):
                await self.bot.send_message(channel,"Back in action are we ? %s ?"%after_member.name)
        if(str(old_status) == "offline"):
            if(str(new_status) == "online"):
                await self.bot.send_message(channel,"Welcome to Developers %s. Hope you enjoy your stay."%after_member.name)
    

def setup(bot):
    n = BabiCog(bot)
    bot.add_listener(n.on_message_listener, "on_message")
    bot.add_listener(n.on_member_update_listener,"on_member_update")
    bot.add_cog(n)
