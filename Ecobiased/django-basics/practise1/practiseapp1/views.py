from django.shortcuts import render
from django.views import View
from .models import Author, Book, Employee, Manager, SaraswatiVidyaMandir, Man, Post
from django.http import HttpResponse
from django.db.models import Q
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from django.shortcuts import render
from .serializers import AuthorSerializer
from django.views.generic import ListView, DetailView

# Create your views here.
class BookView(View):

    def get(self, request):
        authors = Author.objects.all()
        books = Book.objects.all()
        print("authors", authors)
        print("Books", books)
        book = Book.objects.select_related("author").get(id=1)
        print("book", book)
        print("author", book.author)
        return render(request, 'index.html')


class ManagerView(View):

    def get(self, request):
        employees = Employee.objects.all()
        managers = Manager.objects.all()
        print("employees", employees)
        print("managers", managers)
        managers1 = Manager.objects.filter(Q(company__icontains='co') & Q(employees__name__startswith='emp'))
        print("managers1", managers1)
        managers = Manager.objects.prefetch_related('employees')
        for manager in managers:
            print("employees", manager.employees.all())
        return HttpResponse("I am from get method of ManagerView.")


class SaraswatiVidyaMandirView(View):

    def get(self, request):
        saraswati_vidya_mandir = SaraswatiVidyaMandir.objects.select_related('school').get(id=1)
        print("saraswati_vidya_mandir", saraswati_vidya_mandir.school)
        mans = Man.objects.prefetch_related('persons')
        mans1 = Man.objects.filter(Q(name__icontains='ma') & Q(name__startswith='ma'))
        print("mans1", mans1)
        for man in mans:
            print("persons", man.persons.all())
        return HttpResponse("I am from get method of SaraswatiVidyaMandir.")


class SessionView(View):

    def get(self, request):
        request.session['username1'] = 'Ashish'
        user_name = request.session.get('username1', 'guest')
        print("user_name", user_name)
        return HttpResponse("I am in get method of SessionView")


@receiver(post_save, sender=Author)
def send_email(sender, instance, created, **kwargs):
    print("I am from sender email.")
    print("sender", sender)
    print("instance", instance)
    print("created", created)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


@receiver(pre_init, sender=Author)
def access_model(sender, *args, **kwargs):
    print("I am from access model")
    print("sender", sender)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


class AuthorView(View):

    def post(self, request):
        author = Author()
        author.name = 'CustomAuthor1'
        author.save()
        return HttpResponse("Author created successfully.")

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        print("data", serializer.data)
        return HttpResponse("I am from author serializers.")


class PostListView(ListView):

    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


