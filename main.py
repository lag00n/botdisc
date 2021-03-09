## feito pelo murilao boladao. github.com/lag00n

import discord 
from discord.ext import commands, tasks
import hostingsetup
import info
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
    await client.change_presence(activity=discord.Game(name="iasmin na minha cama"))
    print('Conectado com sucesso como:', client.user)

@client.command()
async def iasmin(ctx):
    await ctx.send(random.choice(things.iasmin))

@client.command()
async def say(ctx, *, arg: str): ## * e arg:str permitem o não uso de aspas.
  await ctx.send(arg)

@client.command()
async def revsay(ctx, *, arg: str):
  await ctx.send (arg[::-1])

@client.command()
async def moeda(ctx):
  rand_int = random.randint(0, 1)
  if rand_int == 0:
    resultado = "Cara"
  else:
    resultado = "Coroa"
  await ctx.send(resultado)

@client.command(name='erase', help='esse commando apaga mensagens')
async def erase(ctx, amount = 10):
  await ctx.send("Apagando Mensagens")
  await ctx.channel.purge(limit=amount)

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if "delben" in message.content:
    await message.channel.send("delben macaco wtf :monkey:")
     
  await client.process_commands(message)

 
hostingsetup.host()
client.run(os.getenv('TOKEN'))