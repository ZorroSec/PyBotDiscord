import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('bot is ready')
    await bot.tree.sync()

@bot.event
async def on_message(msg: discord.Message):
    await bot.process_commands(msg)

from app.commands import *