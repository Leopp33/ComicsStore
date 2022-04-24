from django.db import models

# Create your models here.
from django.db import models

from comics_store.users.models import User

# Create your models here.

def Comic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=2048)
    onsaleDate = models.DateField()