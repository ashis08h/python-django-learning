from django.db import models


class Author(models.Model):

    name = models.CharField(max_length=250)


class Book(models.Model):

    name = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Employee(models.Model):

    name = models.CharField(max_length=250, null=False)


class Manager(models.Model):

    company = models.CharField(max_length=250, default='dummy')
    employees = models.ManyToManyField(Employee)


class Post(models.Model):

    title = models.CharField(max_length=250)
    description = models.TextField()


class School(models.Model):

    # whenever we create an entry or we update an entry establishment time will update.
    establishment = models.DateTimeField(auto_now=True)
    # Whenever we create an entry created date will store as current date but will not change
    # incase of update.
    created_date = models.DateTimeField(auto_now_add=True)
    principal = models.CharField(max_length=250, verbose_name='Principal_of_the_school')


class SaraswatiVidyaMandir(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Person(models.Model):
    height = models.FloatField()


class Man(models.Model):
    name = models.CharField(max_length=250)
    persons = models.ManyToManyField(Person)


class Woman(models.Model):
    name = models.CharField(max_length=250)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)




