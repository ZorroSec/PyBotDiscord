import discord
from discord.ext import commands
from config import bot

@bot.event
async def on_ready():
    print('bot is ready')
    await bot.tree.sync()

@bot.event
async def on_message(msg: discord.Message):
    await bot.process_commands(msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

bot.run('MTA3MDUzNTM0NDQ0NzAyOTI3OA.GtCpSu.Lz-6Lz-_V9VUyhBm4HTjHRV0uIjYvYFas4VbVU')