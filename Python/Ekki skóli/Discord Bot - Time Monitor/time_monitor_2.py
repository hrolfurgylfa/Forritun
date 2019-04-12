import discord
from discord.ext import commands

token_file_name = "token.txt"
def saekjaToken():
    token_file = open(token_file_name, "r")
    token = token_file.read()
    token_file.close()
    return token

client = discord.Client()

allar_channels = client.get_all_channels()

# @client.event
# async def on_ready():
#     print('Started up as:',bot.user.name)

@client.event
async def on_message(message):
    if message.content.find("?who") != -1:
        await message.channel.send("This is Mr. Bot")
        

token = saekjaToken()
client.run(token)

