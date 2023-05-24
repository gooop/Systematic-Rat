"""
SYSTEMATIC RAT:
A discord bot that is written for the rats discord server

Originally written for Systematic Rat
https://github.com/gooop/Systematic-Rat

Copyright 2023 Gavin Castaneda
"""

# ==== Includes ====
import discord
from Helpers import Helpers as hp
from discord.ext import commands
import asyncio
import os

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


# ==== Cog Methods ====
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'- Loaded cog: {filename[:-3]}')
            except Exception as e:
                hp.eprint(f'- Failed to load cog: {filename[:-3]}: {e}')


async def unload_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.unload_extension(f'cogs.{filename[:-3]}')
                print(f'- Unloaded cog: {filename[:-3]}')
            except Exception as e:
                hp.eprint(f'- Failed to unload cog: {filename[:-3]} : {e}')


@bot.command(name='reload_cogs',
                    help='Reloads cogs/extensions.',
                    hidden=True,
                    brief='Reloads cogs/extensions.')
async def reload_cogs(context):
    #TODO: Permissions check
    await unload_cogs()
    await load_cogs()
    await context.send('Cogs reloaded.')


# ==== Main ====
async def main():
    await load_cogs()
    await bot.start(TOKEN)

asyncio.run(main())
