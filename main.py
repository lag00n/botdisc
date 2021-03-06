import discord
import os
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    print('Login feito com sucesso como: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!henrique'):
        await message.channel.send('henrique viadinho')

    if message.content.startswith('!felix'):
        await message.channel.send('felix baitola')

    if message.content == "delben":
      await message.channel.send('macaco do caralho esse delben')
  
client.run(os.getenv('TOKEN'))