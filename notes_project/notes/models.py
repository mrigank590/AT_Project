from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
