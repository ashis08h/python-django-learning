from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Employee(models.Model):
    name = models.CharField(max_length=200)


class Manager(models.Model):
    company = models.CharField(max_length=200)
    employees = models.ManyToManyField(Employee)


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


class School(models.Model):
    establishment = models.DateTimeField()
    principal = models.CharField(max_length=200)


class SaraswatiVidyaMandir(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Person(models.Model):
    height = models.FloatField()


class Man(models.Model):
    name = models.CharField(max_length=200)
    persons = models.ManyToManyField(Person)


class Woman(models.Model):
    name = models.CharField(max_length=200)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

