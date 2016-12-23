import discord
import asyncio

#change id accordingly for other channels
#general : 252122196707770369
#testing : 252375277076873216

#channel_id = #ChannelID

#change it to your bot token
#bot_token = #token here;

channel = discord.Object(channel_id)
client = discord.Client()
onlineMembers = []
onlineMembersUpdated = []

async def welcome_new_online_member():
    """Welcomes any member who has come online"""

    await client.wait_until_ready()
    while not client.is_closed:

        #get online members
        for server in client.servers:
            for member in server.members:
                if member.status == discord.Status.online or member.status == discord.Status.idle:
                    onlineMembers.append(str(member))
                    print("old "+str(member))

        await asyncio.sleep(1)

        #get online members after 1 second
        for server in client.servers:
            for member in server.members:
                if member.status == discord.Status.online or member.status == discord.Status.idle:
                    onlineMembersUpdated.append(str(member))
                    print("new "+str(member))

        #compare the two lists
        await compare_and_display(onlineMembers,onlineMembersUpdated)
        del onlineMembers[:]
        del onlineMembersUpdated[:]
        print("####################################")


async def compare_and_display(oldList,newList):
    """Function to compare two lists and send welcome message to only member who has come online"""

    if len(oldList) < len(newList):
        count = 0
        for val in oldList:
            if val in newList:
                print(val+" present in both list")
                count = count + 1
            if count == len(oldList):
                newMembersCount = len(newList)-len(oldList)
                for x in range(newMembersCount):
                    await display_welcome_message(newList[x-newMembersCount])


async def display_welcome_message(newOnlineMember):
    """Displays a welcome message"""

    welcome_message = "Welcome " +newOnlineMember +" to the Developer Server. Hope you enjoy your stay here! "
    await client.send_message(channel, welcome_message)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(welcome_new_online_member())
client.run(bot_token)
