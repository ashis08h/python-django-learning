from django.contrib import admin
from .models import Author, Man, Woman, Person, SaraswatiVidyaMandir,\
    Post, School, Employee, Book, Manager, Product

# Register your models here.

admin.site.register(Author)
admin.site.register(Man)
admin.site.register(Person)

admin.site.register(Woman)
admin.site.register(School)
# admin.site.register(Post)

admin.site.register(Book)
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(Product)
admin.site.register(SaraswatiVidyaMandir)

class PostAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.using('new')

    def save_model(self, request, obj, form, change):
        obj.save(using='new')
admin.site.register(Post, PostAdmin)