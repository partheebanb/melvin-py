import discord
from discord.ext import commands

import requests
from dotenv import load_dotenv
import os
import datetime
from dateutil.parser import parse
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf

load_dotenv()
alphavantageKey = os.environ.get("ALPHAVANTAGE_KEY")

class OHLCHistory():

    def __init__(self, dates=[], opens=[], highs=[], lows=[], closes=[]):
        self.dates = dates
        self.opens = opens
        self.highs = highs
        self.lows = lows
        self.closes = closes





class Candlestick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def plot(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid plot command passed...')

    @plot.command(aliases=['t'])
    async def today(self, ctx, ticker):
        return

    @plot.command(aliases=['w'])
    async def week(self, ctx, ticker):
        return

    @plot.command(aliases=['m'])
    async def month(self, ctx, ticker):
        ticker = ticker.upper()

    @plot.command(aliases=['q'])
    async def quarter(self, ctx, ticker):
        ticker = ticker.upper()

    @plot.command(aliases=['y'])
    async def year(self, ctx, ticker):
        ticker = ticker.upper()

    @plot.command(aliases=['y2d'])
    async def ydt(self, ctx, ticker):
        ticker = ticker.upper()

def setup(client):
    client.add_cog(Candlestick(client)) 