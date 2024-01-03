import discord
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import os
import logging
import logging.handlers


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
#client = discord.Client(intents=intents)


streamerID = "6021"
streamUrl = f"https://www.streamersonglist.com/t/miametzmusic/history?p=all"
streamAPI = f"https://api.streamersonglist.com/v1/streamers/{streamerID}/playHistory?size=50&current=0&type=playedAt&order=desc&period=all&songId=null"


@bot.command()
async def songs(ctx):
     


    logging.getLogger('discord.client').info("CMD:Songs")
    await ctx.send("CMD:songs")
    await get_song_history(ctx)
    




async def get_song_history(ctx):
    url = streamAPI
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print(data)
                # Process and send data to channel
            else:
                print("Failed to retrieve data:", response.status)
                await ctx.send("Failed to retrieve data")




@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    
    
    if message.author == bot.user:        
        print("EXIT ME")
        return

    #print(message)
    print("MSG-RX:",message.content)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)
    


# Load token from environment variable for security
load_dotenv()
token = os.getenv("TOKEN")
if not token:
    raise ValueError("No token provided. Set the TOKEN environment variable.")



bot.run(token)


