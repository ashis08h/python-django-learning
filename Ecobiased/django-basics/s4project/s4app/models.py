from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=200)


class Book(models.Model):

    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Employee(models.Model):

    name = models.CharField(max_length=200, null=False)


class Manager(models.Model):

    name = models.CharField(max_length=200, default='dummy')
    employee = models.ManyToManyField(Employee)


class Post(models.Model):

    title = models.CharField(max_length=200)
    description=models.TextField()


class School(models.Model):

    # whenever we create or update this table establishment will change.
    establishment = models.DateTimeField(auto_now=True)
    # whenever we create an entry create_date will come but will not update if we update this model.
    create_date = models.DateTimeField(auto_now_add=True)
    principal = models.CharField(max_length=200, verbose_name='Principal of the school')


class SaraswatiVidyaMandir(models.Model):

    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Person(models.Model):

    height=models.FloatField()


class Man(models.Model):

    name = models.CharField(max_length=200)
    person = models.ManyToManyField(Person)


class Woman(models.Model):

    name = models.CharField(max_length=200)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)


class Product(models.Model):

    name = models.CharField(max_length=200)
    desc = models.TextField()

    def clean(self):

        super().clean()
        if self.name == 'forbidden':
            raise ValidationError(f"{self.name} is not allowed.")


def validate_not_forbidden_name(value):
    if value == 'test':
        raise ValidationError("The test name is not allowed")


class Product1(models.Model):

    name = models.CharField(max_length=200, validators=[validate_not_forbidden_name])
    desc = models.TextField()


class NoteBook(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publish_date = models.DateField()

    def __str__(self):
        return self.title





