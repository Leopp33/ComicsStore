from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

def User(models.Model):
    # id = models.IntegerField(max_length=100)
    name = models.CharField(max_length=55)
    age = models.IntegerField(max_length=3)
    password = models.CharField(max_length=128)

def Token(models.Model):
    token = models.CharField(max_length=256)