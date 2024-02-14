from django.shortcuts import render
from .models import Book, Author, Employee, Manager, Post, SaraswatiVidyaMandir, Man
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.db.models import Q
from .serializers import AuthorSerializer
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver

# Create your views here.


class BookView(View):

    def get(self, request):
        authors = Author.objects.all()
        books = Book.objects.all()
        print("books", books)
        print("authors", authors)
        book = Book.objects.select_related("author").get(id=1)
        print(book.author)
        return HttpResponse("This is a list of books.")


class ManagerView(View):

    def get(self, request):
        employees = Employee.objects.all()
        managers = Manager.objects.all()
        managers1 = Manager.objects.filter(Q(employees__name__startswith='a') & Q(company__icontains='d'))
        print("employees", employees)
        print("managers", managers)
        print("managers1", managers1)
        manager_list = Manager.objects.prefetch_related('employees')
        print("manager_list", manager_list)
        for manager in manager_list:
            print("employees", manager.employees.all())
        my_dict = {'name': 'ashish'}
        return render(request, 'index.html', context=my_dict)


class SessionView(View):

    def post(self, request):
        request.session['username1'] = 'Ashish'
        return HttpResponse('Successfully stored the data into session.')

    def get(self, request):
        username1 = request.session.get('username1', 'guest')
        return HttpResponse(f'Successfully fetched the data from the session. {username1}')


class AuthorView(View):

    def post(self, request):
        author_obj = Author()
        author_obj.name = 'Rabindra nath'
        author_obj.save()
        return HttpResponse(f'Successfully saved the author name {author_obj.name}.')

    def get(self, request):
        authors = Author.objects.all()
        serialize_author = AuthorSerializer(authors, many=True)
        print("serializers", serialize_author.data)
        return HttpResponse('Get list of all the authors in the serialized way.')


class PostListView(ListView):

    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):

    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'


class SaraswatiView(View):

    def get(self, request):
        saraswati = SaraswatiVidyaMandir.objects.select_related('school').get(id=1)
        print("school", saraswati.school)
        mans = Man.objects.prefetch_related('person')
        print('mans', mans)
        for man in mans:
            print('persons', man.person.all())
        return HttpResponse("Get Saraswati school list")


@receiver(pre_init, sender=Author)
def access_modal(sender, *args, **kwargs):
    print("I am accessing model")
    print("sender", sender)
    print("args", args)
    for key, value in kwargs.items():
        print("key", key, "value", value)


@receiver(post_save, sender=Author)
def send_email(sender, instance, created, **kwargs):
    print("I am sending email")
    print("sender", sender)
    print("instance", instance)
    print("created", created)
    for key, value in kwargs.items():
        print(f"{key}:{value}")



