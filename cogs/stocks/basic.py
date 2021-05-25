import discord
from discord.ext import commands

import requests
from dotenv import load_dotenv
import os

load_dotenv()
alphavantageKey = os.environ.get("ALPHAVANTAGE_KEY")
ameritradeKey = os.environ.get("AMERITRADE_KEY")

class StocksBasic(commands.Cog):

    def __init__(self, client):
        self.client = client

    def getDataFromAlpha(self, data):

        for key in data:
            data = data[key]
            break

        return (f"Open: {data['1. open']} \n" +
                        f"Low: {data['3. low']} \n" +
                        f"High: {data['2. high']} \n" +
                        f"Close: {data['5. adjusted close']} \n" + 
                        f"Volume: {data['6. volume']} \n")


    @commands.command()
    async def quote(self, ctx, ticker):
        ticker = ticker.upper()
        endpoint = f"https://api.tdameritrade.com/v1/marketdata/{ticker}/quotes"
        payload = {'apikey': ameritradeKey"}

        response = requests.get(url = endpoint, params= payload)

        data = response.json()[ticker]
        await ctx.send(f"The last price was: {data['lastPrice']}")

    @commands.command()
    async def today(self, ctx, ticker):
        ticker = ticker.upper()
        endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={alphavantageKey}"
        response = requests.get(url = endpoint)

        data = response.json()['Time Series (Daily)']

        await ctx.send(self.getDataFromAlpha(data))

    @commands.command()
    async def week(self, ctx, ticker):
        ticker = ticker.upper()
        endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={ticker}&apikey={alphavantageKey}"
        response = requests.get(url = endpoint)

        data = response.json()['Weekly Adjusted Time Series'][0]

        await ctx.send(self.getDataFromAlpha(data))

    @commands.command()
    async def month(self, ctx, ticker):
        ticker = ticker.upper()
        endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={ticker}&apikey={alphavantageKey}"
        response = requests.get(url = endpoint)

        data = response.json()['Monthly Adjusted Time Series'][0]

        await ctx.send(self.getDataFromAlpha(data))

    @commands.command()
    async def quarter(self, ctx):
        await ctx.send('allo')

    @commands.command()
    async def year(self, ctx):
        await ctx.send('allo')

    @commands.command()
    async def ytd(self, ctx):
        await ctx.send('allo')

def setup(client):
    client.add_cog(StocksBasic(client)) 