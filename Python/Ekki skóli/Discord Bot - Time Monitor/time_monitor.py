import discord
from discord.ext import commands

token_file_name = "token.txt"

token_file = open(token_file_name, "r")
token = token_file.read()
token_file.close()
print("Token:|"+token+"|")

client = discord.Client()
bot = commands.Bot(command_prefix='?', case_insensitive=True, description="...")

allar_channels = client.get_all_channels()

# Bot channel
# channel = message.channel

@bot.event
async def on_ready():
    print('Started up as:',bot.user.name)

@bot.event
async def on_message(message):
    message_content_lower = message.content.lower()
    print(message_content_lower)
    if message_content_lower.startswith("?who"):

        allar_channels.send("Return")
        # await bot.send_message("Joining voice channel: |"+message.content[5::]+"|")
        # try:
        #     channelID = client.get_channel(message.content[5::])
        #     await bot.send_message("ChannelID: |"+channelID+"|")
        #     await client.join_voice_channel(channelID)
        #     # await bot.send_message(allir_members)
        # except IndexError:
        #     await bot.send_message("Please send in a second argument with the ?who command saying what channel should be looked at.")

@bot.command()
async def hello():
    """This commands makes the bot respond with hello when you say hello"""
    await bot.say('Hello!')

bot.run(token)

