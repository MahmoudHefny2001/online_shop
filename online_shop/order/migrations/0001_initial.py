# Generated by Django 4.1.5 on 2023-02-17 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        ('cart', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('order_tracking_number', models.CharField(db_index=True, max_length=100, unique=True)),
                ('order_taxes', models.FloatField(default=50)),
                ('order_state', models.CharField(choices=[('Arrived', 'Arrived'), ('Not Arrived', 'Not Arrived')], max_length=12)),
                ('order_code', models.CharField(max_length=200, unique=True)),
                ('estimated_delivery_time', models.DateField()),
                ('total_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.address')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_orders', to='location.address')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_orders', to='product.product')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
