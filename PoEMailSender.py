import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from config import *

class PoeMailSender:
    def __init__(self, senderEmail):
        self.senderEmail = senderEmail
        self.password = emailPassword

    def connect(self):
        self.server = smtplib.SMTP('smtp.gmail.com',587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.senderEmail, self.password)

    def disconnect(self):
        self.server.quit()

    def sendMail(self, targetMail, subject="", body=""):
        msg = MIMEMultipart()
        msg['From'] = self.senderEmail
        msg['To'] = targetMail
        msg['Subject'] = subject
        messageBody = body
        msg.attach(MIMEText(messageBody, 'plain'))
        text = msg.as_string()
        self.server.sendmail(self.senderEmail, targetMail, text)
