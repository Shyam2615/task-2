from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics')
    address_line1 = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set'  
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set_permissions'  
    )

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)