from django.db import models

# Create your models here.

CHOICES = (('IT', 1), ('Non IT', 2), ('Mobiles Phones', 3))


class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=CHOICES)
    added_date =  models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
