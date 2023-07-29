# BigRegBot.py
#import os

#import discord


#load_dotenv()
# loads from .env file
#TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()

import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
# loads from .env file
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(TOKEN)
