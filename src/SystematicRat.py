import discord
from discord.ext import commands
import asyncio
import os
import sys

# ==== Helpers ====
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

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
