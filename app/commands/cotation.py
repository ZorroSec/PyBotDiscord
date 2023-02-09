from app import *
from requests import get

@bot.command()
async def cotation(ctx):
    cot = get(f"https://economia.awesomeapi.com.br/last/BTC-BRL").json()
    await ctx.send(cot['BTCBRL'])
