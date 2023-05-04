import discord
from discord.ext import commands     
import typing
import random
import asyncio
import os


# ==== Setup ====
# Get token from current directory
TOKEN = ''
with open('../token.txt', 'rt') as f:
    TOKEN = f.read()
    f.close()

# Manage intents and connect to discord
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# List servers bot is connected to
@bot.event
async def on_ready():
    print(f'\n{bot.user} is connected to the following servers:')
    for guild in bot.guilds:
        print(f'{guild.name} (id: {guild.id})')


# ==== Import cogs ====
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    

# ==== Main ====
async def main():
    await load_cogs()
    await bot.start(TOKEN)

asyncio.run(main())
