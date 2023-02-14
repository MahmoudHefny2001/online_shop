import stripe
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from payments import RedirectNeeded, get_payment_model
from rest_framework import generics, mixins, status, views, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from location.serializers import AddressSerializer
from order.models import Order, OrderItem
from product.models import Product

from . import models, serializers
from .tasks import Payment_mail, payment_completed

stripe.api_key = settings.STRIPE_SECRET_KEY

# class PaymentViewSet(viewsets.ModelViewSet):
#     queryset = models.Payment.objects.all()
#     serializer_class = serializers.PaymentSerializer

#     def get_queryset(self, *args, **kwargs):
        
#         qs = super().get_queryset(*args, **kwargs)
#         return qs.filter(id = self.request.user.customer.id)


class CreateStripeCheckoutSession(views.APIView):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        try:
            product = Product.objects.get(id=product_id)
            checkout_session = stripe.checkout.Session.create(
                line_items = [
                    {
                        'price_data': {
                            'currency': '',
                            'unit_amount': product.price,
                            'product_data': {
                                'name': product.name,
                                'image': product.image,
                                'description': product.description,
                                'inventory': product.inventory
                            },
                        },
                        'quantity': OrderItem.quantity,
                    }
                ],

                mode = 'payment',
                metadata = {

                }
            )

        except Exception:
            return Response({'message':'something went wrong while creating your payment','error':str(e)}, status=500)



@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, settings.STRIPE_SECRET_WEBHOOK
        )
    except ValueError as e:
        return Response(status=400)
    except stripe.error.SignatureVerificationError as e:
        return Response(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        print(session)
        customer_email = session['customer_details']['email']
        product_id=session['metadata']['product_id']
        product = Product.objects.get(id=product_id)
        
        Payment_mail()


        PaymentHistory.objects.create(product=product, payment_status=True)
    return HttpResponse(status=200)