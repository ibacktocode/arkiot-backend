from django.db import models
# from django.contrib.auth import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import users.utils as SmsVerify
import random

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone_number:
            raise ValueError('The given phone number must be set')
        # email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        SmsVerify.request_code(phone = phone_number, app_hash = '#ABC')
        # utils.send_sms_verification(to=phone_number,body='Your verification code is ' + str(random.randint(000000,999999)))
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField( max_length=30, blank=True)
    date_of_birth = models.DateTimeField(null=True)
    gender = models.CharField(max_length=2, blank=True)
    country = models.CharField( max_length=5, blank=True)
    date_joined = models.DateTimeField( auto_now_add=True)
    is_staff = models.BooleanField( default=True)
    is_active = models.BooleanField( default=True)
    status = models.CharField(max_length=30, blank=False, default='unverified')

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    class Meta:
        db_table = 'user'

class Sms:
    def __init__(self, **kwargs):
        for field in ('otp'):
            setattr(self, field, kwargs.get(field, None))
