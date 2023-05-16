import discord
from discord.ext import commands     
import random

class Casino(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='balance',
                help = 'Give the Casino balance of all rats!',
                brief = 'Rats balance.')
    