import discord
import json
import os
import random
import requests

from discord.ext import commands

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_location = os.path.join(__location__, 'keys.json')

intents = discord.Intents.default()
intents.members = True

description = '''An example bot to showcase the discord.ext.commands extension
module.'''

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

with open(file_location, "r") as f:
    my_dict = json.load(f)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def ominous_picture(self, ctx):
    """gets omnious giphy"""
    giphy_token = my_dict['giphy']
    r = await requests.get('https://api.giphy.com/v1/gifs/random?api_key={giphy_token}&tag=ominous&rating=g')
    await ctx.send(r)
    
    


bot.run(my_dict['botToken'])