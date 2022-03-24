import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

discord_token = os.getenv('DISCORD_TOKEN')
bot.run(discord_token)