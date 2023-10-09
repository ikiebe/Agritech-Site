from django.db import models

# Create your models here.
class Table(models.Model):
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    #description = models.TextField()
    #id = models.UUIDField(primary_key=True)