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
    def __init__(self):
        pass