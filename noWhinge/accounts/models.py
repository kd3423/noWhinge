from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserCustom(AbstractUser):
	contact = models.CharField(max_length=100)
	locality = models.CharField(max_length=100,blank=True)


