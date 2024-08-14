from django.contrib import admin
from .models import Author, Man, Woman, Person, SaraswatiVidyaMandir,\
    Post, School, Employee, Book, Manager

# Register your models here.

admin.site.register(Author)
admin.site.register(Man)
admin.site.register(Person)

admin.site.register(Woman)
admin.site.register(School)
admin.site.register(Post)

admin.site.register(Book)
admin.site.register(Employee)
admin.site.register(Manager)

admin.site.register(SaraswatiVidyaMandir)