# Generated by Django 4.1.5 on 2023-02-14 12:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('description', models.TextField(default='', max_length=500)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='product.category')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='discount.discount')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='merchant.inventory')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('customer', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
    ]
