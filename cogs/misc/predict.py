import discord 
from discord.ext import commands
import random

class Predict(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def predict(self, ctx):
        responses = ['It is Certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                #  'Reply hazy, try again.',
                #  'Ask again later.',
                #  'Better not tell you now.',
                #  'Cannot predict now.',
                #  'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    
        await ctx.send(random.choice(responses))

def setup(client):
    client.add_cog(Predict(client))