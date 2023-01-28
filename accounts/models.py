from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from accounts.phone_code import phone_codes, sorted_phone_codes
# Create your models here.

from django.conf import settings


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager




class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(_('email address'), unique=True)
    country_code = models.CharField(choices=sorted_phone_codes, max_length=40, default='91')
    contact_no =  models.CharField(_('Enter Your Contact Number..'), null = False, blank = False, max_length=15)
    full_name = models.CharField(_('Full Name'), max_length=25)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['country_code', 'contact_no']
    objects = CustomUserManager()

    def __str__(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    full_name =models.CharField( max_length=50, default="")

    def __str__(self):
        return f'Profile for user {self.user.username}'
