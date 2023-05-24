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
import typing

# ==== Class ====
class Email(commands.Cog):
    # ==== Init ====
    def __init__(self, bot):
        self.bot = bot
        self.mailbox = EmailClass()
        self.parsed_emails = []
        self.thread_ids = []


    # ==== Methods ====
    async def send_to_threads(self, message):
        """Prints message in all threads that have been added to thread_ids
        
        Args:
            message (str): message to send"""
        print(f'- [Email] send_to_threads called.')
        for thread_id in self.thread_ids:
            thread = await self.bot.fetch_channel(thread_id)
            await thread.send(message)

    @tasks.loop(minutes=5.0)
    async def print_emails(self):
        """Paginates, then calls send_to_threads to print emails in all threads added to thread_ids."""
        print(f'- [Email] print_emails called.')
        if self.parsed_emails is not None:
            for email in self.parsed_emails:
                sendString = "📧 New email! 📧\n > Author: " + email['author'] + " \n > Subject: " + email['subject'] + "\n```" + email['body'] + "```"

                if len(sendString) > 2000:
                    try:
                            message_length = 2000 - 19 # 19 is len("``` \n ``` (100/100)")
                            pages = int(len(sendString) / message_length)
                            for i in range(pages):
                                if i == 0:
                                    await self.send_to_threads(f"{sendString[0:message_length]} \n ``` ({i + 1}/{pages})") 
                                elif i != pages:
                                    await self.send_to_threads(f"``` {sendString[message_length * i:(message_length * i) + message_length]} \n ``` ({i + 1}/{pages})")
                                else:
                                    await self.send_to_threads(f"``` {sendString[message_length * i:]} \n ``` ({i + 1}/{pages})")

                    except Exception as e:
                        print(f"- [Email] failed to paginate message more than 2000 chars: {e}")

                else:
                    try:
                        await self.send_to_threads(sendString)
                    except Exception as e:
                        print(f"- [Email] failed to send message less than 2000 chars: {e}")


        else:
            print(f'- [Email] no emails to send.')
            #await context.send(f"No emails found.")
        
        # Clear emails now that they've been printed.
        self.parsed_emails = []


    # ==== Tasks ====
    @tasks.loop(minutes=2.5)
    async def check_email(self, mark_read=True):
        """Checks email every 2.5 minutes"""
        #TODO: logging levels
        print(f'- [Email] check_email called.')

        # Get unread emails
        self.emails = await self.mailbox.get_emails()
        self.parsed_emails = await self.mailbox.parse_emails(self.emails, mark_read)
        

    # ==== Commands ====
    @commands.command(name='setup_email',
                hidden=True,
                help='Starts email checking task. Must be run for emails to be checked every 5 minutes.',
                brief='Starts email checking task.')
    async def email_setup(self, context):
        """Begins timers for timed methods and adds threads from callers to thread_ids."""
        author = context.message.author
        print(f'- [Email] !setup_email called by {author}')
        await context.message.delete()

        # Add thread to list of threads to send emails to
        thread_id = context.channel.id
        self.thread_ids.append(thread_id)
        print(f'- [Email] thread id {thread_id} added to list of threads.')

        # Start timers and tell server success
        await context.send("Success! I am going to begin checking for and printing emails...")
        self.check_email.start()
        self.print_emails.start()


    @commands.command(name='checkemails',
                help='Forces bot to check emails',
                brief='Forces bot to check emails')
    async def checkemails(self, context, 
                          mark_read : typing.Optional[bool],):
        author = context.message.author
        print(f'- [Email] !checkemails called by {author}')
        await context.send("Checking emails...")
        await self.check_email(mark_read)
    

    @commands.command(name='printemails',
                help='Forces bot to print emails',
                brief='Forces bot to print emails')
    async def printemails(self, context):
        author = context.message.author
        print(f'- [Email] !printemails called by {author}')
        await context.send("Printing emails...")
        await self.print_emails()
    

# ==== Setup ====
async def setup(bot):
    await bot.add_cog(Email(bot))