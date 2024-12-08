from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Employee(AbstractUser):

    mobile_no = models.IntegerField(max_length=13, unique=True)
    
    



