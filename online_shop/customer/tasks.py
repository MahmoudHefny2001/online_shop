from celery import shared_task, Task
from django.conf import settings

from django.core.mail import send_mail, send_mass_mail

# 

@shared_task
def send_registration_mail(email):
    print(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD, settings.EMAIL_HOST)
    send_mail('Registration mail', 'Thanks for using our services', settings.EMAIL_HOST_USER, [email,], fail_silently=False)
    return None
