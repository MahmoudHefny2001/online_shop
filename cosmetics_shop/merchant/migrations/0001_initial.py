# Generated by Django 4.1.5 on 2023-02-06 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(blank=True, max_length=50, null=True)),
                ('line2', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, default='Assiut', max_length=30)),
                ('governorate', models.CharField(blank=True, default='Assiut', max_length=30, null=True)),
                ('zipCode', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(db_index=True, max_length=15, unique=True)),
                ('postal_code', models.CharField(max_length=30)),
                ('fax', models.CharField(max_length=20)),
                ('email', models.CharField(db_index=True, max_length=200, unique=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant.address')),
            ],
        ),
    ]
