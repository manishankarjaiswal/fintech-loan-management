from flask_mail import Message
from app import mail

def send_email(subject, body):
    """Utility function to send an email."""
    to="csmanishankar@gmail.com"
    msg = Message(subject, recipients=[to])
    msg.body = body
    mail.send(msg)
