from django.db import models
from django.contrib.auth.models import(
    User, AbstractUser, 
    AbstractBaseUser, UserManager,
    PermissionsMixin, BaseUserManager
)
from django.core.validators import RegexValidator
from django.utils import timezone
from location.models import Address


# Create your models here.




class Customer(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=False, null=False)
    email = models.CharField(max_length=250, unique=True, blank=False, null=False)
    full_name = models.CharField(max_length=250, unique=False)
    phone_number = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=250, blank=False, null=False)

    cart = models.OneToOneField('cart.Cart', on_delete = models.PROTECT, blank=True, null=True)


    def __str__(self):
        return self.username 
    

class Profile(models.Model):
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male', null=True, blank=False)
    customer = models.OneToOneField('customer.Customer', on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.FileField(upload_to='users', blank=True, null=True)
    address = models.ForeignKey('location.Address', on_delete=models.CASCADE, null=True, blank=True, default='')
    