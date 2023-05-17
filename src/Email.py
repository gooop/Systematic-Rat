"""
EMAILS CLASS:
Class for connecting to gmail and extracting email contents.

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

# ==== Class ====
class Email:
    # ==== Init ====
    def __init__(self):
        self._mailbox = self._setup_mailbox()

    # ==== Member Variables ====
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    # ==== Methods ====
    def _setup_mailbox(self):
        """Sets up credentials for Gmail API
        
        Returns:
            mailbox (googleapiclient.discovery.Resource): mailbox Resource built by Gmail API
        """
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
            raise HttpError
        
        return mailbox


    def get_emails(self):
        """Checks for new emails

        Returns:
            emails (dict): Dictionary of unread emails 
        """
        try:
            # Get unread emails
            emails = self._mailbox.users().messages().list(userId='me', q='is:unread').execute()
        except Exception as e:
            print(f'Error in get_emails: {e}')
            raise Exception
        return emails
    

    def parse_emails(self, emails, read=True):
        """Parses a list of emails and returns author, subject, and contents
        
        Args:
            emails (dict): Dictionary of email ids returned by get_emails
            read (bool): Flag to decide whether to mark emails as read

        Returns:
            parsed_emails (list of dicts): List of emails (dict) that contains author, subject, and contents.
        """
        # Pull message ids out of email 
        email_ids = [msg['id'] for msg in emails.get('messages', [])]

        # The actual content of the emails (to, from, subject, message, etc.)
        emails_meat = []
        for email_id in email_ids:
            email_meat = self._mailbox.users().messages().get(userId='me', id=email_id).execute()
            emails_meat.append(email_meat)
        
   
        # Get subject
        parsed_emails = []
        for email in emails_meat:
            headers = email['payload']['headers']
            author = [header['value'] for header in headers if header['name'] == 'From'][0]
            subject = [header['value'] for header in headers if header['name'] == 'Subject'][0]
            import pdb
            pdb.set_trace()
            #TODO: Maybe render contents out to pdf? Check pdfkit (pdfkit.from_file, or other method might work)
            #contents = 
        


# def main():
#     email = Email()
#     mailbox = email.setup_mailbox()
#     unparsed_emails = email.get_emails(mailbox)
#     parsed_emails = email.parse_emails(mailbox, unparsed_emails)
    

# if __name__ == '__main__':
#     main()
