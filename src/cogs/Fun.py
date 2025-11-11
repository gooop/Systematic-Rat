"""
FUN COG:
A discord bot Cog that contains silly commands

Originally written for Systematic Rat
https://github.com/gooop/Systematic-Rat

Copyright 2023 Gavin Castaneda
"""

# ==== Includes ====
import discord
from discord.ext import commands     
import random


# ==== Cog ====
class Fun(commands.Cog):
    # ==== Init ====
    def __init__(self, bot):
        self.bot = bot


    # ==== Commands ====
    @commands.command(name='ratspin',
                    help='Uploads an image of a spinning rat or falls back onto pasting a URL',
                    brief='SPEEN')
    async def ratspin(self, context):
        # Delete command from user and log
        author = context.message.author
        print(f'- [Fun] !ratspin called by {author}')
        author = str(author).split('#')[0]
        await context.message.delete()

        # Try to upload, if that fails, paste URL
        try:
            with open('../assets/rat-spinning.gif', 'rb') as f:
                picture = discord.File(f)
                await context.send(f'{author} says: SPEEN', file=picture)
        except:
            image_url = "https://media.tenor.com/aaEMtGfZFbkAAAAi/rat-spinning.gif'"
            await context.send(image_url)

# ==== Setup ====
async def setup(bot):
    await bot.add_cog(Fun(bot))