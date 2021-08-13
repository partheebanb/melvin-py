import discord
from discord.ext import commands

# github: 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

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

    def __init__(self, data):
        self.dates = data.keys()
        self.opens = []
        self.highs = []
        self.lows = []
        self.closes = []
        self.volumes = []

        for key in self.dates:
            self.opens.append(float(data[key]["1. open"]))  
            self.highs.append(float(data[key]["2. high"]))
            self.lows.append(float(data[key]["3. low"]))
            self.closes.append(float(data[key]["4. close"]))
            self.volumes.append(float(data[key]["5. volume"]))

    def getDF(self):
        d = {
            'Open' : self.opens,
            'High' : self.highs,
            'Low' : self.lows,
            'Close' : self.closes,
            'Volume' : self.volumes
        }
        dateTimeIndex = pd.to_datetime(pd.Index(self.dates))
        df = pd.DataFrame(data=d, index=dateTimeIndex)
        return df




class Candlestick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['c'])
    async def candlestick(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid plot command passed...')

    @candlestick.command(aliases=['t'])
    async def today(self, ctx, ticker):
        endpoint = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
        response = requests.get(url = endpoint)
        data = response.json()["Time Series (5min)"]

        # obtain df containing data in the appropriate format for MPL Finance
        ohlcHistory = OHLCHistory(data)

        df = ohlcHistory.getDF()

        mpf.plot(df)
        mpf.savefig('temp.png')
        await ctx.send(file=discord.File('temp.png'))

        # return

    @candlestick.command(aliases=['w'])
    async def week(self, ctx, ticker):
        return

    @candlestick.command(aliases=['m'])
    async def month(self, ctx, ticker):
        ticker = ticker.upper()

    @candlestick.command(aliases=['q'])
    async def quarter(self, ctx, ticker):
        ticker = ticker.upper()

    @candlestick.command(aliases=['y'])
    async def year(self, ctx, ticker):
        ticker = ticker.upper()

    @candlestick.command(aliases=['y2d'])
    async def ydt(self, ctx, ticker):
        ticker = ticker.upper()

def setup(client):
    client.add_cog(Candlestick(client)) 