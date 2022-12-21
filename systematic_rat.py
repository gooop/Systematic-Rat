import discord
from discord.ext import commands     
import typing

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
    print(f'\n{client.user} is connected to the following guilds:')
    for guild in client.guilds:
        print(f'{guild.name} (id: {guild.id})')


# ==== Commands ====
@client.command(name='hello',
                help='Systematic rat is here to help!',
                brief='Says hello.')
async def hello(context):
    await context.send("Hello, ratlings! I am here to take your jobs.")


@client.command(name='multipoll',
                help='Makes a poll with multiple options (NOT IMPLEMENTED)',
                brief='Makes a poll with multiple options (NOT IMPLEMENTED)')
async def multipoll(context, 
                    ping : typing.Optional[bool],
                    duration_days : typing.Optional[int],
                    message : str,
                    *args):
    #TODO: include args that can be used in !help
    # Delete command from user and log
    author = context.message.author
    print(f'!poll called by {author}')
    await context.message.delete()


@client.command(name='poll',
                help="Makes a poll with two options",
                brief="Makes a poll with two options",
                usage='!poll <ping: 1 | 0 | > <duration_days: NOT IMPLEMENTED> <message: string>')
async def poll(context, 
                ping : typing.Optional[bool],
                duration_days : typing.Optional[int],
                *,
                message : str):
    # Delete command from user and log
    author = context.message.author
    print(f'!poll called by {author}')
    await context.message.delete()
    
    # Blank message error
    if message == '':
        await context.send('Usage: !poll <ping: 1 | 0 | > <duration_days: NOT IMPLEMENTED> <message>')
        return
    
    # Send message
    if ping:
        msg = await context.send(f'**POLL:** \n{message} \n@everyone')
    else:
        msg = await context.send(f'**POLL:** \n{message}')
    
    # Set up for poll
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")


@client.command(name='ratspin',
                help='Uploads an image of a spinning rat or falls back onto pasting a URL',
                brief='SPEEN')
async def ratspin(context):
    # Delete command from user and log
    author = context.message.author
    print(f'!ratspin called by {author}')
    author = str(author).split('#')[0]
    await context.message.delete()

    # Try to upload, if that fails, paste URL
    try:
        with open('rat-spinning.gif', 'rb') as f:
            picture = discord.File(f)
            await context.send(f'{author} says SPEEN', file=picture)
    except:
        image_url = "https://media.tenor.com/aaEMtGfZFbkAAAAi/rat-spinning.gif'"
        await context.send(image_url)

    

# ==== Run bot ====
client.run(TOKEN)