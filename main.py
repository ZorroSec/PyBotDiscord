import discord
from discord.ext import commands
from config import bot
from commands import pong 

@bot.event
async def on_ready():
    print('bot is ready')
    await bot.tree.sync()

@bot.event
async def on_message(msg: discord.Message):
    await bot.process_commands(msg)

@bot.command()
async def ping(ctx):
    await pong(ctx)


bot.run('MTA3MDUzNTM0NDQ0NzAyOTI3OA.Gr8AXJ.4-IXbHHgjkSyAjA86k2SnHyZRkmNEK8tWr9VCo')