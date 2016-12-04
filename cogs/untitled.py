#!/usr/bin/env python3
 
"A simple discord.py program to log in and receive and post messages"
 
# Configure these for a valid Discord account to log in as
email = FILL IN EMAIL
password = FILL IN PASSWORD
 
# Logging configuration. Go to DEBUG level if you want much more detail
import logging
logging.basicConfig(level=logging.INFO)
 
import discord, asyncio
 
# Create a subclass of Client that defines our own event handlers
# Another option is just to write functions decorated with @client.async_event
class MyClient(discord.Client):
    @asyncio.coroutine
    def on_ready(self):
        "Asynchronous event handler for when we are fully ready to interact with the server"
        print('Logged in %s %s' % (self.user.name, self.user.id))
 
        # Store a couple of destinations for messages
        nelson = None
        gamesChannel = None
 
        # Enumerate the channels. This works over all servers the user is participating in
        print('Channels')
        for channel in self.get_all_channels():
            print(' ', channel.server, channel.name, channel.type)
            if channel.name == "games":
                # Store away the #games channel object for later use
                gamesChannel = channel
 
        # Enumerate the members for every serv
        print('Members')
        for member in self.get_all_members():
            print(' ', member.name, member.status)
            if member.name == "Nelson":
                nelson = member
 
        # Send a message to a destination
        yield from self.send_message(nelson, "Hello meatbag")
 
    @asyncio.coroutine   
    def on_message(self, message):
        "Asynchronous event handler that's called every time a message is seen by the user"
        print('Message received\n ', message.content)
 
# Run the client, a blocking call that logs in and runs the event loop. Exits on Ctrl-C
client = MyClient()
client.run(email, password)