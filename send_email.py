import smtplib, ssl
import os

def send_email(user_email,message):
    host = "smtp.gmail.com"
    port = 465
    password = os.getenv('PORTFOLIO_PASSWORD')
    receiver = "boyercoding@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(receiver, password)
        server.sendmail(user_email, receiver, message)