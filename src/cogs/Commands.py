import discord
from discord.ext import commands     
import typing
import random

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='hello',
                help='Systematic rat is here to help!',
                brief='Says hello.')
    async def hello(self, context):
        await context.send("Hello, ratlings! I am here to take your jobs.")

async def setup(bot):
    await bot.add_cog(Commands(bot))