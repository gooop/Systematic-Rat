"""
UTILS COG:
A discord bot Cog that contains useful commands

Originally written for Systematic Rat
https://github.com/gooop/Systematic-Rat

Copyright 2023 Gavin Castaneda
"""

# ==== Includes ====
import discord
from discord.ext import commands     
import typing

# ==== Cog ====
class Utils(commands.Cog):
    # ==== Init ====
    def __init__(self, bot):
        self.bot = bot

    # ==== Commands ====
    @commands.command(name='hello',
                help='Systematic rat is here to help!',
                brief='Says hello.')
    async def hello(self, context):
        await context.send("Hello, ratlings! I am here to take your jobs.")


    @commands.command(name='announce',
                    help='Announce something!',
                    brief='Announce something!',
                    usage='Usage: !announce <ping: 1 | 0 | > <message>')
    async def announce(self,
                        context, 
                        ping : typing.Optional[bool],
                        *,
                        message : str):
        # Delete command from user and log
        author = context.message.author
        print(f'- [Utils] !announce called by {author}')
        await context.message.delete()

        # Blank message error
        if message == '':
            await context.send('Usage: !announce <ping: 1 | 0 | > <message>')
            return
        
        # Send message
        if ping:
            msg = await context.send(f'**📢📢📢 ANNOUNCEMENT 📢📢📢** \n{message} \nsent by {author}. @everyone')
        else:
            msg = await context.send(f'**📢📢📢 ANNOUNCEMENT 📢📢📢** \n{message} \nsent by {author}.')


    @commands.command(name='multipoll',
                    help='Makes a poll with multiple options',
                    brief='Makes a poll with multiple options',
                    usage='Usage: !multipoll <options_num: [1, 10]> <ping: 1 | 0 | > <duration_days: NOT IMPLEMENTED> <message>')
    async def multipoll(self,
                        context, 
                        options_num : int,
                        ping : typing.Optional[bool],
                        duration_days : typing.Optional[int],
                        *,
                        message : str):
        #TODO: include args that can be used in !help
        # Delete command from user and log
        author = context.message.author
        print(f'- [Utils] !multipoll called by {author}')
        await context.message.delete()

        # Blank message error
        if message == '':
            await context.send('Usage: !multipoll <options_num: [1, 10]> <ping: 1 | 0 | > <duration_days: NOT IMPLEMENTED> <message>')
            return
        
        # Send message
        if ping:
            msg = await context.send(f'**POLL:** \n{message} \nsent by {author}. @everyone')
        else:
            msg = await context.send(f'**POLL:** \n{message} \nsent by {author}.')
        
        emoji_list = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

        for i in range(options_num):
            await msg.add_reaction(emoji_list[i])


    @commands.command(name='poll',
                    help="Makes a poll with two options",
                    brief="Makes a poll with two options",
                    usage='!poll <ping: 1 | 0 | > <duration_days: NOT IMPLEMENTED> <message: string>')
    async def poll(self,
                    context, 
                    ping : typing.Optional[bool],
                    duration_days : typing.Optional[int],
                    *,
                    message : str):
        # Delete command from user and log
        author = context.message.author
        print(f'- [Utils] !poll called by {author}')
        await context.message.delete()
        
        # Blank message error
        if message == '':
            await context.send('Usage: !poll <ping: 1 | 0 | > <duration_days: NOT IMPLEMENTED> <message>')
            return
        
        # Send message
        if ping:
            msg = await context.send(f'**POLL:** \n{message} \nsent by {author}. @everyone')
        else:
            msg = await context.send(f'**POLL:** \n{message} \nsent by {author}.')
        
        # Set up for poll
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")


    @commands.command(name='schedule',
                    help="Makes a post with multiple options for scheduling",
                    brief="Makes a post with multiple options for scheduling",
                    usage='!schedule <ping: 1 | 0 | > <duration_days: NOT IMPLEMENTED> <message: string>')
    async def schedule(self,
                    context, 
                    ping : typing.Optional[bool],
                    duration_days : typing.Optional[int],
                    *,
                    message : str):
        #TODO: Extend to create an event after x number of days/seconds or whatever
        # Delete command from user and log
        author = context.message.author
        print(f'- [Utils] !schedule called by {author}')
        await context.message.delete()
        
        # Blank message error
        if message == '':
            await context.send('Usage: !schedule <ping: 1 | 0 | > <duration_days: NOT IMPLEMENTED> <message>')
            return
        
        # Send message
        if ping:
            msg = await context.send(f'**EVENT:** \n{message} \nsent by {author}. @everyone')
        else:
            msg = await context.send(f'**EVENT:** \n{message} \nsent by {author}.')
        
        # Set up for poll
        await msg.add_reaction("🇸")
        await msg.add_reaction("🇺")
        await msg.add_reaction("🇲")
        await msg.add_reaction("🇹")
        await msg.add_reaction("🇼")
        await msg.add_reaction("🇷")
        await msg.add_reaction("🇫")


# ==== Setup ====
async def setup(bot):
    await bot.add_cog(Utils(bot))