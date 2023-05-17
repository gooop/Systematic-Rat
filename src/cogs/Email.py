"""
EMAILS COG:
A discord bot Cog that allows you to check an email inbox and forward
those messages to a discord server

Originally written for Systematic Rat
https://github.com/gooop/Systematic-Rat

Copyright 2023 Gavin Castaneda
"""

# ==== Includes ====
from discord.ext import tasks, commands
import Email

# ==== Class ====
class Email(commands.Cog):
    # ==== Init ====
    def __init__(self):
        pass


    # ==== Tasks ====
    @tasks.loop(minutes=5.0)
    async def check_email(self):
        """Checks email every 5 minutes"""
        pass
        # TODO: Check email stuff here