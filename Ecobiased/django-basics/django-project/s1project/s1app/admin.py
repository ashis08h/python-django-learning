from django.contrib import admin
from .models import Person, Man, Woman, School, SaraswatiVidyaMandir, Employee, Manager, Post, Book, Author

# Register your models here.
admin.site.register(Person)
admin.site.register(Man)
admin.site.register(Woman)
admin.site.register(School)
admin.site.register(SaraswatiVidyaMandir)
admin.site.register(Employee)
admin.site.register(Book)
admin.site.register(Author)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']


class ManagerAdmin(admin.ModelAdmin):
    list_display = ['company']
    list_filter = ['company']


admin.site.register(Post, PostAdmin)
admin.site.register(Manager, ManagerAdmin)

