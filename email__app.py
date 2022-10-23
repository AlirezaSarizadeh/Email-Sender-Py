import ssl
import smtplib
from email.message import EmailMessage
email__sender = "itsarizade@gmail.com"
email__password = "wutvwahzgracczvx"
email__reciver = "rekeh40004@cadolls.com"
subject = "Dont Forget Who You Are !"
body = "I Believe In You MAN ! Just Keep Going ..."

em = EmailMessage()
em['From'] = email__sender
em['To'] = email__reciver
em['Subject']= subject
em.set_content(body)

Context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=Context) as smtp:
    smtp.login(email__sender,email__password)
    smtp.sendmail(email__sender,email__reciver,em.as_string())