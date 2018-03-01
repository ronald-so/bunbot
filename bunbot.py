import discord
import asyncio
import json
from discord.ext import commands
from datetime import datetime

import search as src
import serverstatus as ss

# Config files
bot = commands.Bot(command_prefix='!')
config = json.load(open('config.json'))
emoji = json.load(open('emoji.json'))

# Discord bot token
token = config['token']

# Emoji
bunemoji = emoji['bun']
bunsleepy = emoji['bunsleepy']
bunangry = emoji['bunangry']
buneating = emoji['buneating']
buncrying = emoji['buncrying']
bunpoo = emoji['bunpoo']
bunhi = emoji['bunhi']
bunpuke = emoji['bunpuke']
bunbook = emoji['bunbook']

# Terraria info
terraria_ip = config['terraria_ip']
terraria_port = config['terraria_port']
terraria_pw = config['terraria_pw']


@bot.event
async def on_ready():
    now = str(datetime.now())
    print('Logged in as ' + bot.user.name)
    print('Bot User ID: ' + bot.user.id)
    print(now[:-7])
    print('------')


@bot.group(pass_context=True)
async def bun(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say(bunemoji)


@bun.command()
async def sleepy():
    await bot.say(bunsleepy)


@bun.command()
async def angry():
    await bot.say(bunangry)


@bun.command()
async def eating():
    await bot.say(buneating)


@bun.command()
async def crying():
    await bot.say(buncrying)


@bun.command()
async def poo():
    await bot.say(bunpoo)


@bun.command()
async def hi():
    await bot.say(bunhi)


@bun.command()
async def puke():
    await bot.say(bunpuke)


# Terraria server status and info
@bun.command()
async def terraria(arg=None):
    if arg == 'info':
        await bot.say('Server IP: `' + terraria_ip + '`\nPort: `' + str(terraria_port) + '`\nPassword: `'
                      + terraria_pw + '`')
    if arg == 'status':
        await bot.say(ss.terraria_status())
    if arg == None:
        await bot.say('`!bun terraria info` - displays server info\n`!bun terraria status` - displays server status')


# Search image on google
@bun.command()
async def give(*, arg):
    await bot.say(bunbook + '\n' + src.imagesearch(arg))

# Search text on google
@bun.command()
async def search(*, arg):
    await bot.say(bunbook*3 + '\n\n' + src.textsearch(arg))

bot.run(token)
