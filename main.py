from dotenv import load_dotenv
import os

import discord 
from discord.ext import commands

# set prefix to /
client = commands.Bot(command_prefix='/')

# get bot token 
load_dotenv()
token = os.environ.get("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
    print('Melvin is running :)')

# load cogs
for root, directories, files in os.walk('./cogs'):

    for directory in directories:

        for filename in os.listdir(f'./cogs/{directory}'):

            if filename.endswith('.py'):
                # remove .py from filename
                client.load_extension(f'cogs.{directory}.{filename[:-3]}')


if __name__ == '__main__':
    client.run(token)
