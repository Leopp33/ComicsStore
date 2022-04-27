# Create your models here.
from djongo import models

# Create your models here.

class User(models.Model):
    # id = models.IntegerField(max_length=100)
    username = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    age = models.IntegerField()
    password = models.CharField(max_length=128)

class Token(models.Model):
    token = models.CharField(max_length=256)
    
# Comenzar bloque para añadir usuario predeterminado.
# e = User()



