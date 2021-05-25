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

class Plot(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.locator = mdates.AutoDateLocator(minticks=7, maxticks=25)
        self.formatter = mdates.ConciseDateFormatter(self.locator)


    def getCanvas(self, w, l):
        fig, axs = plt.subplots(1, 1, constrained_layout=True, figsize=(w, l))
        axs.xaxis.set_major_locator(self.locator)
        axs.xaxis.set_major_formatter(self.formatter)

        return fig, axs

    # @commands.Cog.listener('stock')
    # async def today(self, ctx):
    #     await ctx.send('allo')

    @commands.group()
    async def plot(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid plot command passed...')

    @plot.command()
    async def today(self, ctx, ticker):
        return

    @plot.command()
    async def week(self, ctx, ticker):
        return

    @plot.command()
    async def month(self, ctx, ticker):
        ticker = ticker.upper()

        # endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={alphavantageKey}"
        endpoint = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
        response = requests.get(url = endpoint)        
        data = response.json()['Time Series (Daily)']

        dates = list(parse(date) for date in data.keys())[:22]
        prices = list(float(price['4. close']) for price in data.values())[:22]

        df = pd.DataFrame(list(zip(dates, prices)),
               columns =['Dates', 'Prices'])

        fig, axs = self.getCanvas(12, 6)
        axs.set_title(f"Last month's prices for {ticker}")
        axs.plot(dates, prices)
        fig.savefig('temp.png')

        # mpf.plot(df)
        # mpf.savefig('mpf.png')

        await ctx.send(file=discord.File('axs.png'))


    @plot.command()
    async def quarter(self, ctx, ticker):
        return
    
    @plot.command()
    async def year(self, ctx, ticker):
        return

    @plot.command()
    async def ytd(self, ctx, ticker):
        endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={alphavantageKey}"
        response = requests.get(url = endpoint)        
        data = response.json()['Time Series (Daily)']

        dates = list(parse(date) for date in data.keys())
        prices = list(float(price['4. close']) for price in data.values())

        fig, axs = self.getCanvas(15, 6)
        axs.set_title(f'YTD for {ticker}')
        axs.plot(dates, prices)
        fig.savefig('temp.png')

        await ctx.send(file=discord.File('temp.png'))
    
    @plot.command()
    async def custom(self, ctx, days, ticker):
        return

def setup(client):
    client.add_cog(Plot(client)) 