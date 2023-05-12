import discord
from Helpers import Helpers as hp
from discord.ext import commands
import asyncio
import os
import sys

# ==== Helpers ====
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# ==== Setup ====
# Get token from current directory
try:
    TOKEN = hp.open_file('../token.txt')
except Exception as e:
    print(f"Error getting token: {e} \n You may need to make a token.txt.")
    exit(-1)

# Manage intents and connect to discord
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# List servers bot is connected to
@bot.event
async def on_ready():
    print(f'\n- {bot.user} is connected to the following servers:')
    for guild in bot.guilds:
        print(f'\t{guild.name} (id: {guild.id})')


# ==== Import cogs ====
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'- Loaded cog: {filename[:-3]}')
            except Exception as e:
                eprint(f'- Failed to load cog: {filename[:-3]}')
                eprint(e)


# ==== Main ====
async def main():
    await load_cogs()
    await bot.start(TOKEN)

asyncio.run(main())
