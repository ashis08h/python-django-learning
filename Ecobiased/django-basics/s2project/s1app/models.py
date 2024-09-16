from django.db import models
from django.core.exceptions import ValidationError


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

# approach 1
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()


    # def clean(self):
    #     # call the parent class clean to maintain built-in validation.
    #     super().clean()
    #     print("come here")
    #     if self.name == 'ForbiddenName':
    #         print("come here 2")
    #         raise ValidationError({"name": "The name \"forbidden\" is not allowed."})

# approach 2
def validate_not_forbidden_name(value):
    if value == 'test':
        raise ValidationError('The name test is not allowed.')

class Product(models.Model):
    name = models.CharField(max_length=200, validators=[validate_not_forbidden_name])
    description = models.TextField()

    def __str__(self):
        return self.name

# approach 3

# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#
#     def clean_name(self):
#         if self.name == 'test':
#             raise ValidationError("The name test is not allowed.")
#
#     def __str__(self):
#         return self.name


class NoteBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title









