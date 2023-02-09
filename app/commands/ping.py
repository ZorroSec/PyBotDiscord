import discord
from discord.ext import commands
from app import bot

@bot.command()
async def ping(ctx):
    await ctx.send('pong!!')


