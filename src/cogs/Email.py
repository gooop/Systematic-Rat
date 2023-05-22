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
        self.parsed_emails = []


    # ==== Methods ====
    async def print_emails(self, context):
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
                                    await context.send(f"{sendString[0:message_length]} \n ``` ({i + 1}/{pages})") 
                                elif i != pages:
                                    await context.send(f"``` {sendString[message_length * i:(message_length * i) + message_length]} \n ``` ({i + 1}/{pages})")
                                else:
                                    await context.send(f"``` {sendString[message_length * i:]} \n ``` ({i + 1}/{pages})")

                    except Exception as e:
                        print(f"- [Email] failed to paginate message more than 2000 chars: {e}")

                else:
                    try:
                        await context.send(sendString)
                    except Exception as e:
                        print(f"- [Email] failed to send message less than 2000 chars: {e}")


        else:
            await context.send(f"No emails found.")


    # ==== Tasks ====
    @tasks.loop(minutes=5.0)
    async def check_email(self, mark_read=False):
        """Checks email every 5 minutes"""
        #TODO: logging levels
        print(f'- [Email] check_email called.')

        # Get unread emails
        self.emails = await self.mailbox.get_emails(mark_read)
        self.parsed_emails = await self.mailbox.parse_emails(self.emails)


    # ==== Commands ====
    @commands.command(name='setup_email',
                hidden=True,
                help='Starts email checking task. Must be run for emails to be checked every 5 minutes.',
                brief='Starts email checking task.')
    async def email_setup(self, context):
        author = context.message.author
        print(f'- [Email] !email_setup called by {author}')
        await context.send("Begin checking for emails...")
        self.check_email.start()


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