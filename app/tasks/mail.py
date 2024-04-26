from flask_mail import Message
from celery import shared_task
from app.extensions import mail
from app.logger import logger


@shared_task
def send_mail(subject: str, to_email: str, message: str) -> None:
    msg = Message(subject, recipients=[to_email], html=message)
    
    try:
        mail.send(msg)

    except Exception as err:
        logger.error(err, exc_info=True)
        
