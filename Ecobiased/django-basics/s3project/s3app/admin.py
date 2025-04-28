from django.contrib import admin
from s3app.models import Author, Book, Employee, Manager, Post, SaraswatiVidyaMandir, School,\
Person, Man, Woman, Post, NoteBook


# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Employee)
admin.site.register(Man)
admin.site.register(Manager)
# admin.site.register(Post)
admin.site.register(SaraswatiVidyaMandir)
admin.site.register(School)
admin.site.register(Person)
admin.site.register(Woman)
admin.site.register(NoteBook)


class PostAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.using('new_database')

    def save_model(self, request, obj, form, change):
        obj.save(using='new_database')

# command to migrate the non default db is python manage.py migrate --database='new_database'


admin.site.register(Post, PostAdmin)

