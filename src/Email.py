"""
EMAILS:
Integrates emails into Systematic Rat

Originally written for Systematic Rat
https://github.com/gooop/Systematic-Rat

Copyright 2023 Gavin Castaneda
"""

# ==== Includes ====
import imaplib
import email
from Helpers import Helpers as hp
from cryptography.fernet import Fernet

# ==== Setup ====
# Connect to the Gmail IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com')

# Setup cypher for email/password
KEY = hp.open_file('../key.txt')

cipher_suite = Fernet(KEY)

# Read in encrypted text
encrypted_email = ''
encrypted_password = ''
with open('../email.txt', 'rt') as f:
    lines = f.readlines()
    encrypted_email = lines[0].strip()
    encrypted_password = lines[1].strip()
    f.close()

# Decrypt
EMAIL = cipher_suite.decrypt(encrypted_email)
PASSWORD = cipher_suite.decrypt(encrypted_password)

# Login to email
mail.login(EMAIL, PASSWORD)

mail.select('inbox')