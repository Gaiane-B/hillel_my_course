import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Configuration_file


# Function for sending e-mails
def sending_mails(recipient: list, message_to_recipient: str) -> object:
    server = Configuration_file.SMTP_SERVER
    PASSWORD = Configuration_file.PASSWORD_API
    USER = Configuration_file.USER_

    recipient = [*recipient]
    sender = USER
    subject = 'What is the current weather in your city? (Gaiane Budarieva)'
    text = message_to_recipient
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipient)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'decorator'

    part_text = MIMEText(text, 'plain')
    msg.attach(part_text)

    mail = smtplib.SMTP_SSL(server)
    mail.login(USER, PASSWORD)
    mail.sendmail(sender, recipient, msg.as_string())
    mail.quit()
    return True
