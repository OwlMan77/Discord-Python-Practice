import discord
import json
import os

from discord.ext import commands

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

client = discord.Client()

file_location = os.path.join(__location__, 'keys.json')

with open(file_location, "r") as f:
    my_dict = json.load(f)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(my_dict['botToken'])