# iwuitnegmizawbgu
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "qinxiaoshu1994@gmail.com"
email_password = 'bwzvcjkoqnbnrgpa'

email_receiver = 'chenbin@chalmers.se'

subject = 'Do not forget to subscribe'
body = """
When you watch a video
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
