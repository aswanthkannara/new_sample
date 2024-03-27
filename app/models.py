from django.db import models

# Create your models here.
class SchoolDetails(models.Model):
    school_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pin = models.CharField(max_length=90)

