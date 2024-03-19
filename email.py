import smtplib, ssl
import random
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "tanmaykarra@gmail.com"
name= ("tanmay bla")
receiver_email = input("enter your email:")
password =("orpuswztusadbgcd")
message = ("""\
Subject:sent by Tanmay Karra
This is just a test email.(,otp)""")
otp = random.randint(1000, 9999)
otp = str(otp)
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)