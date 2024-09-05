from django.db import models

# Create your models here.
class registration(models.Model):
    NAME = models.CharField(max_length=100)
    FATHERS_NAME = models.CharField(max_length=100)
    MOTHERS_NAME = models.CharField(max_length=100)
    DOB = models.DateField(auto_now= False,auto_now_add=False)
    EMAIL = models.EmailField(max_length=100)
    CONTACT = models.IntegerField()
    PINCOAD= models.IntegerField()
    ADDRESS = models.CharField(max_length=200)

