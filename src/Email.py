"""
EMAILS:
Integrates emails into Systematic Rat

Originally written for Systematic Rat
https://github.com/gooop/Systematic-Rat

Copyright 2023 Gavin Castaneda
"""

# ==== Includes ====
import os
from Helpers import Helpers as hp
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Email:
    # ==== Init ====
    def __init__(self):
        self.setup_mailbox()

    # ==== Member Variables ====
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    # ==== Methods ====
    def setup_mailbox(self):
        """Sets up credentials for Gmail API"""
        # Begin: Lifted from quickstart.py on https://developers.google.com/gmail/api/quickstart/python
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '..\credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        # End: Lifted from quickstart.py on https://developers.google.com/gmail/api/quickstart/python

        # Begin: code written by Gavin
        try:
            # Call the Gmail API
            mailbox = build('gmail', 'v1', credentials=creds)
        except HttpError as e:
            print(f'Error in setup_credentials: {e}')
        
        return mailbox


    def get_emails(self, mailbox):
        """Checks for new emails
        
        Args:
            mailbox (googleapiclient.discovery.Resource): the mailbox setup by the Gmail API

        Returns:
            dict: Dictionary of unread emails 
        """
        try:
            # Get unread emails
            emails = mailbox.users().messages().list(userId='me', q='is:unread').execute()
            import pdb
            pdb.set_trace()
        except Exception as e:
            print(f'Error in get_emails: {e}')
        return emails
    

    def parse_emails(self, mailbox, emails):
        """Parses a list of emails and returns author, subject, and contents
        
        Args:
            mailbox (googleapiclient.discovery.Resource): the mailbox setup by the Gmail API
            emails (dict): Dictionary of emails

        Returns:
            string: author string
            string: subject string
            string: contents string
        """


def main():
    email = Email()
    mailbox = email.setup_mailbox()
    unparsed_emails = email.get_emails(mailbox)
    

if __name__ == '__main__':
    main()
