## feito pelo murilao boladao. github.com/lag00n

import discord 
from discord.ext import commands, tasks
import hostingsetup
import things 
import os
import random

key = os.getenv('key')
wkey = os.getenv('wkey')

client = commands.Bot( # deveria trocar o nome pra bot? ao invés de client.
  command_prefix = 'mu!',
  case_insensitive=True
  )

client.author_id = 740276491094327356
client.remove_command('help')

@client.event
async def on_ready():
    print('Conectado com sucesso como:', client.user)

@client.command()
async def iasmin(ctx):
    await ctx.send(random.choice(things.iasmin))

@client.command()
async def say(ctx, *, arg: str): ## * e arg:str permitem o não uso de aspas.
  await ctx.send(arg)

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if "delben" in message.content:
    await message.channel.send("delben macaco wtf :monkey:")
     
  await client.process_commands(message)
 
hostingsetup.host()
client.run(os.getenv('TOKEN'))