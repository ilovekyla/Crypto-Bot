import discord
from discord.ext import commands
import requests
import os

client = commands.Bot(command_prefix = '.', help_command=None)

@client.command()
async def crypto(ctx, crypto):
	btc = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
	eth = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'
	xrp = 'https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD'
	doge = 'https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD'

	btc_request = requests.get(url=btc)
	btc_json = btc_request.json()

	eth_request = requests.get(url=eth)
	eth_json = eth_request.json()

	xrp_request = requests.get(url=xrp)
	xrp_json = xrp_request.json()

	doge_request = requests.get(url=doge)
	doge_json = doge_request.json()

	btc_price = btc_json['USD']
	eth_price = eth_json['USD']
	xrp_price = xrp_json['USD']
	doge_price = doge_json['USD']

	if crypto == "btc":
		await ctx.send(f"BTC is currently at ${btc_price}")
	elif crypto == "eth":
		await ctx.send(f"ETH is currently at ${eth_price}")
	elif crypto == "xrp":
		await ctx.send(f"XRP is currently at ${xrp_price}")
	elif crypto == "doge":
		await ctx.send(f"Doge is currently at ${doge_price}")

client.run(os.environ['token'])