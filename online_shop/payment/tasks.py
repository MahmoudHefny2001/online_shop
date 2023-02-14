from celery import Task, shared_task
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from order.models import Order
from customer.models import Customer

# @task
# def payment_completed(order_id):
#     """
#     Task to send an e-mail notification when an order is
#     successfully created.
#     """
#     order = Order.objects.get(id=order_id)

#     email = send_mail(subject, message, from_email, recipient_list)

@shared_task()
def Payment_mail(email):
    send_mail(
        'Payment sucessful', 'Thanks for your purchase, Your order is ready.', settings.EMAIL_HOST_USER, [email,], fail_silently=False
    )
                   