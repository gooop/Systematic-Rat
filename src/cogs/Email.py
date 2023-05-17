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
from Email import Email as EmailClass

# ==== Class ====
class Email(commands.Cog):
    # ==== Init ====
    def __init__(self, bot):
        self.bot = bot
        self.mailbox = EmailClass()

    
    # ==== Methods ====
    async def print_emails(self, context):
        print(f'- [Email] print_emails called.')
        if self.parsed_emails is not None:
            for email in self.parsed_emails:
                await context.send(f"Author: {email['author']}")
                await context.send(f"Author: {email['subject']}")
        else:
            print('Else')
            await context.send(f"No emails found.")


    # ==== Tasks ====
    @tasks.loop(minutes=5.0)
    async def check_email(self):
        """Checks email every 5 minutes"""
        #TODO: logging levels
        print(f'- [Email] check_email called.')

        # Get unread emails
        self.emails = await self.mailbox.get_emails()
        self.parsed_emails = await self.mailbox.parse_emails(self.emails)

    # ==== Commands ====
    @commands.command(name='checkemails',
                help='Forces bot to check emails',
                brief='Forces bot to check emails')
    async def checkemails(self, context):
        author = context.message.author
        print(f'- [Email] !checkemails called by {author}')
        await context.send("Checking emails...")
        await self.check_email()
    

    @commands.command(name='printemails',
                help='Forces bot to print emails',
                brief='Forces bot to print emails')
    async def printemails(self, context):
        author = context.message.author
        print(f'- [Email] !printemails called by {author}')
        await context.send("Printing emails...")
        await self.print_emails(context)
    



# ==== Setup ====
async def setup(bot):
    await bot.add_cog(Email(bot))