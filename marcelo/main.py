# Discord Bot: Marcelo (Y Agachate Conocelo)
# Author: Davide D'Angelo

NzgyNjAwNjQ5NzM2MTkyMDAw.X8Ojpg.12e5lkbHGoAiyi5ZlisW1zYlsCQ

import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

users = []
channels = []
# Credentials
load_dotenv('.env')

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='&', help_command=None, intents=intents)

# Metodi di utility
async def sendEmbed(ctx, embed):
    await ctx.send(embed=embed)

async def leave(ctx):
    await ctx.voice_client.disconnect()

#Definition of Embed Commands
embedMarcelo = discord.Embed(
    colour=discord.Colour.red()
)
##Task -> trova la gif, se non la trovi, exception
embedMarcelo.set_image(url='https://media1.tenor.com/images/ec2f2e4c789262bc58d1fea7da20ab4f/tenor.gif?itemid=10983596')

########################################################################################################################

#Event List
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    global channels
    channels = client.get_all_channels()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Il comando inserito non esiste.\n So che sei triste...\n')
        await asyncio.sleep(2)
        await ctx.send('Per questo ti meriti un Marcelo')
        await asyncio.sleep(1)
        await sendEmbed(ctx, embedMarcelo)
    elif isinstance(error, commands.CommandInvokeError):
        print(error)

########################################################################################################################

#Commands List
@client.command(name='marcelo', aliases=['m', 'gif'], pass_context=True)
async def rules(ctx):
    await sendEmbed(ctx, embedMarcelo)

########################################################################################################################

client.run(os.getenv('TOKEN'))

########################################################################################################################
