from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from .models import Author, Book, Employee, Manager, SaraswatiVidyaMandir, Man
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import AuthorSerializer

# Create your views here.


class BookView(View):

    def get(self, request):
        authors = Author.objects.all()
        books = Book.objects.all()
        print("authors", authors)
        print("books", books)

        author1 = Author.objects.filter(id=1)
        print("author1", author1)
        book = Book.objects.select_related('author').get(id=1)
        print("book", book)
        print("author", book.author)
        books = list(Book.objects.filter(id=1).values("author"))
        print("books", books)
        books = list(Book.objects.filter(id=1).values_list("author"))
        print("books", books)
        return HttpResponse("I am from get method of BookView class.")


class ManagerView(View):

    def get(self, request):
        employees = Employee.objects.all()
        managers = Manager.objects.all()
        print("employees", employees)
        print("managers", managers)
        manager = Manager.objects.filter(Q(name__icontains='man') & Q(employee__name__startswith='emp'))
        print("manager", manager)
        managers = Manager.objects.prefetch_related('employee')
        for manager in managers:
            print(manager.employee.all())
        return render(request, 'manager.html', context={'managers': managers})


class SaraswatiVidyaMandirView(View):

    def get(self, request):
        saraswati_vidya_mandir = SaraswatiVidyaMandir.objects.select_related('school').get(id=1)
        print("saraswati_vidya_mandir", saraswati_vidya_mandir)
        mans = Man.objects.prefetch_related('person')
        for man in mans:
            print("persons", man.person.all())
        mans = Man.objects.filter(Q(name__icontains='m') & Q(name__startswith='ma'))
        return render(request, 'saraswati_vidya_mandir.html', context={'mans': mans})


class SessionView(View):

    def get(self, request):
        request.session['username'] = 'ashish'
        print(f"I have stored the session with name {request.session.get('username', None)}")
        return HttpResponse(f"I have stored the session with name {request.session.get('username', None)}")


@receiver(post_save, sender=Author)
def send_email(sender, instance, created, **kwargs):

    print("I am from email send function")
    print("sender", sender)
    print("instance", instance)
    print("created", created)
    for key, value in kwargs.items():
        print("key", key)
        print("value", value)


class AuthorView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        author_obj = Author()
        author_obj.name = "custom_author"
        author_obj.save()
        return HttpResponse(f"Author with id {author_obj.id} created successfully.")

    def get(self, request):

        authors = Author.objects.all()
        author_serializers = AuthorSerializer(authors, many=True)
        print("author_serializers", author_serializers.data)
        return render(request, 'author.html', context={'authors': author_serializers})


