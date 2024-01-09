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

    def __str__(self) -> str:
        return self.name + "-" + self.location


POSITION_CHOICES = (('Manager', 'manager'),
                    ('Software Developer', 'sd'),
                    ('Project Leader', 'pl'))
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

