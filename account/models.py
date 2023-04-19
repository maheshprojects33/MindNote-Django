from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager):
    use_in_migrations = True

    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser Must have is_staff=True")
        
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    email_token = models.CharField(max_length=255, null=True, blank=True)
    forget_password = models.CharField(max_length=255, null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True,null=True, blank=True)
    last_logout = models.DateTimeField(auto_now=True,null=True, blank=True)
    is_verified = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Bio(models.Model):
    country_list = {
        "NP": "Nepal",
        "IN": "India",
        "CH": "China"
    }

    address = models.CharField(max_length=100, blank=True, null=True, default="n/a")
    phone = models.CharField(max_length=15, blank=True,
                             null=True, default="n/a")
    country = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True, default="1990-01-01")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
