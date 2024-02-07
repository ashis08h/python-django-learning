from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Employee(models.Model):
    name = models.CharField(max_length=200, null=False)


class Manager(models.Model):
    company = models.CharField(max_length=200, default='dummy')
    employees = models.ManyToManyField(Employee)


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


class School(models.Model):
    # Whenever we save the object then current date time will store here.
    establishment = models.DateTimeField(auto_now=True)
    # Whenever we create the entries first time in the object that time automatically data will
    # store here and will not update in the update time.
    created_date = models.DateTimeField(auto_now_add=True)
    principal = models.CharField(max_length=200, verbose_name='Principal of school')


class SaraswatiVidyaMandir(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Person(models.Model):
    height = models.FloatField()


class Man(models.Model):
    name = models.CharField(max_length=200)
    person = models.ManyToManyField(Person)


class Woman(models.Model):
    name = models.CharField(max_length=200)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
