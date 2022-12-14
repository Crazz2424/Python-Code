from django.db import models

# Create your models here.

class Useful_links(models.model):
    links = models.CharField(max_length=64)
    
