from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('customer.urls')),
    path('products/', include('product.urls')),
    path('carts/', include('cart.urls')),
    path('orders/', include('order.urls')),
    path('payments/', include('payment.urls')),

    # path('payments/', include('payments.urls')),    ##

    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


