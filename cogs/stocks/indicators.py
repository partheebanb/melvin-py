import discord
from discord.ext import commands

class StocksBasic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.command(aliases=['stock today'])
    def today(self, ctx):
        ctx.send('allo')

def setup(client):
    client.add_cog(StocksBasic(client)) 