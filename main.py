## feito pelo murilao boladao. github.com/lag00n

import discord
from discord.ext import commands, tasks
import hostingsetup
import info
import os
import random

key = os.getenv('key')
wkey = os.getenv('wkey')

client = commands.Bot(  # deveria trocar o nome pra bot? ao invés de client.
    command_prefix='mu!',
    case_insensitive=True)

client.author_id = 740276491094327356
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="iasmin na minha cama"))
    print('Conectado com sucesso como:', client.user)


@client.command()
async def iasmin(ctx):
    if ctx.message.author.id == (504458442300456970):
      await ctx.send(info.iasmin2)
    else:
      await ctx.send(info.iasmin)


@client.command()
async def say(ctx, *, arg: str):  ## * e arg:str permitem o não uso de aspas.
    await ctx.channel.purge(limit=int(1))
    await ctx.send(arg)


@client.command()
async def revsay(ctx, *, arg: str):
    await ctx.channel.purge(limit=int(1))
    await ctx.send(arg[::-1])


@client.command()
async def moeda(ctx):
    rand_int = random.randint(0, 1)
    if rand_int == 0:
        resultado = "Cara"
    else:
        resultado = "Coroa"
    await ctx.send(resultado)


@client.command(name='erase', help='esse commando apaga mensagens')
async def erase(ctx, amount=10 + 2):
    await ctx.send("Apagando Mensagens")
    await ctx.channel.purge(limit=amount)


@client.command()
async def warn(ctx, member: discord.Member, *, msg):
    channel = await member.create_dm()
    await channel.send(msg)

''' isso aqui é ruim porra.
@client.command()
async def flood(ctx, member: discord.Member, *, msg):
    count = 0
    channel = await member.create_dm()
    await channel.send(msg)
    while (count <= 10):  # ou (count <= 10)
        await channel.send(msg)
        if count == 10:
            break
        count += 1
'''
@client.command()
async def flood(ctx, member: discord.Member, nmsg:int, *, msg: str ): 
    channel = await member.create_dm()
    for i in range(nmsg):
      await channel.send(msg)

@client.command()
async def loud(ctx):
    await ctx.send(info.loud2)

@client.command()
async def embed(ctx):
    embed = discord.Embed(title="DELBEN CLICA AQUI",
                          url="https://xvideos.com",
                          description="Delben clica ali .",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if "delben" in message.content:
        await message.channel.send("delben macaco wtf :monkey:")

    #preciso achar um jeito de consertar isso aqui.
    elif "lmao" in message.content:
        await message.add_reaction(info.lmao)

    elif "lmfao" in message.content:
        await message.add_reaction(info.lmao)

    await client.process_commands(message)  # desbuga os outros commandos.


hostingsetup.host()
client.run(os.getenv('TOKEN'))
