import discord
from discord.ext import commands     

# Get token from current directory
TOKEN = ''
with open('token.txt', 'rt') as f:
    TOKEN = f.read()
    f.close()

# Manage intents and connect to discord
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

# List servers bot is connected to
@client.event
async def on_ready():
    for guild in client.guilds:
        print(
   
        f'{guild.name}(id: {guild.id})'
        )


# Commands
@client.command(name='hello')
async def hello(context):
    """Says hello."""
    await context.send("Hello, ratlings! I am here to take your jobs.")
    
# @client.command(name='makeeventpoll')
# async def makeeventpoll(context, *args):
    # if 'name' in args:
        

@client.command(name='ratspin')
async def ratspin(context):
    """SPEEN"""
    try:
        with open('rat-spinning.gif', 'rb') as f:
            picture = discord.File(f)
            await context.send(file=picture)
    except:
        image_url = "https://media.tenor.com/aaEMtGfZFbkAAAAi/rat-spinning.gif'"
        await context.send(image_url)

    

# Run bot
client.run(TOKEN)