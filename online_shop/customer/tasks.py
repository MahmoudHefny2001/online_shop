from celery import shared_task, Task

from django.core.mail import send_mail

# @shared_task
# def send_registration_mail(email):
#     send_mail('Registration mail', 'Thanks for using our services', 'hefny4@gmail.com', ['{email}'], fail_silently=False)
#     return None
