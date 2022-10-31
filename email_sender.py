# Go over to our gmail account and setup 2 factors authentication
from email.message import EmailMessage
from email_password import password
import ssl
import smtplib

email_sender = 'bokanga.kongo@gmail.com'

# Generate app password
email_password = password

email_receiver = 'bokangakongo02@gmail.com'

subject = "Email From Python"
body = """
When you got this message , it's coming from Python File
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

# Create a function to send the mail
