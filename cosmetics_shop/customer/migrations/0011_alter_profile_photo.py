# Generated by Django 4.1.5 on 2023-02-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_address_zipcode_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='users'),
        ),
    ]