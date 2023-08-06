import logging
import os
import smtplib
import ssl

from datetime import datetime
from dotenv import load_dotenv

from email.message import EmailMessage
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flota_app.utils import clear_environment_variables

logging.basicConfig(level=logging.INFO)


class MailingService:

    def __init__(self, mail_env_path: str):
        # This env variables clearance is needed to avoid 'lost'
        # variables from previous loadings of .env if current one does not exist
        clear_environment_variables(['EMAIL', 'PASSWORD', 'PORT', 'SMTP_SERVER'])
        load_dotenv(mail_env_path)
        self.port = int(os.getenv("PORT"))
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.email = str(os.getenv("EMAIL"))
        self.password = str(os.getenv('PASSWORD'))

    def send_mail(self, msg: str, receiver_mail: str, subject: str) -> None:
        message = EmailMessage()
        message['Subject'] = subject
        message['From'] = self.email
        message['To'] = receiver_mail
        message.set_content(msg)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.email, self.password)
            server.send_message(message)
