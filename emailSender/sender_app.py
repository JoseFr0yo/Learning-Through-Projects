# Import the EmailMessage class from the email.message module
from email.message import EmailMessage
# Import the ssl module (Secure Sockets Layer wrapper for socket objects)
import ssl
# Import the smtplib module (Simple Mail Transfer Protocol client)
import smtplib

# Credentials for the email account and recipient (I dont recommend using this for real world use, storing the password here is unsafe, use environment variables instead)
sending_from = 'Your Email Here'
sending_password = 'Enter App Password Here'
recipient = 'example@recipient.com'

# Email parameters
subject = 'This is a test email'
body = """
This is a test email, please ignore it.
"""


emsg = EmailMessage()
emsg['From'] = sending_from
emsg['To'] = recipient
emsg['subject'] = subject
emsg.set_content(body)


# create a context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sending_from, sending_password)
    smtp.sendmail(sending_from, recipient, emsg.as_string())
