import discord
from discord.ext import commands     
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='ratspin',
                    help='Uploads an image of a spinning rat or falls back onto pasting a URL',
                    brief='SPEEN')
    async def ratspin(self, context):
        # Delete command from user and log
        author = context.message.author
        print(f'!ratspin called by {author}')
        author = str(author).split('#')[0]
        await context.message.delete()

        # Try to upload, if that fails, paste URL
        try:
            with open('assets/rat-spinning.gif', 'rb') as f:
                picture = discord.File(f)
                await context.send(f'{author} says: SPEEN', file=picture)
        except:
            image_url = "https://media.tenor.com/aaEMtGfZFbkAAAAi/rat-spinning.gif'"
            await context.send(image_url)


    @commands.command(name='ratcum',
                    hidden=True,
                    brief='What will you get??')
    async def ratcum(self, context):
        # Delete command from user and log
        author = context.message.author
        print(f'!ratcum called by {author}')
        author = str(author).split('#')[0]
        await context.message.delete()

        # Try to upload, if that fails, paste URL
        try:
            rand_int = random.randint(0, 100)
            if rand_int <= 50:
                with open('assets/Top_Rat.jpg', 'rb') as f:
                    picture = discord.File(f)
                    picture.filename = f'SPOILER_{picture.filename}'
                    await context.send(f'{author} says: ~uuhhnnh~', file=picture)
            if rand_int > 50 and rand_int <= 99:
                with open('assets/Bottom_Rat.jpg', 'rb') as f:
                    picture = discord.File(f)
                    picture.filename = f'SPOILER_{picture.filename}'
                    await context.send(f'{author} says: ~uuhhnnh~', file=picture)
            if rand_int == 100:
                with open('assets/Chad_Rat.jpg', 'rb') as f:
                    picture = discord.File(f)
                    picture.filename = f'SPOILER_{picture.filename}'
                    await context.send(f'{author} **ROLLED A RARE RAT!**', file=picture)

        except:
                await context.send('Error: Rat could not finish')


async def setup(bot):
    await bot.add_cog(Fun(bot))