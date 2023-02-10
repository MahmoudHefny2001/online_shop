from celery import shared_task, Task

from django.core.mail import send_mail

@shared_task
def send_registration_mail():
    send_mail('Registration mail', 'Thanks for using our services', 'hefny4@gmail.com', 'mhmwdhfny22@fastmail.com')
    return None
