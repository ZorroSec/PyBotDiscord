from app import bot
from requests import get

@bot.commands()
async def ddd(ctx, ddd):
    req = get(f"https://brasilapi.com.br/api#tag/BANKS/paths/~1banks~1v1/get/ddd/v1/{ddd}").json()
    await ctx.send(req)