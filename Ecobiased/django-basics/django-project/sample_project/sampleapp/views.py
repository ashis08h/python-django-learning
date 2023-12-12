from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Book, Author, Employee, Manager, Post, School, SaraswariVidyaMandir, Person, Man, Woman
from django.db.models import Q
from django.shortcuts import render
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from .serializers import AuthorSerializer


class BookView(View):

    def get(self, request):
        authors = Author.objects.all()
        books = Book.objects.all()
        print("book", books)
        print("authors", authors)
        book = Book.objects.select_related("author").get(id=1)
        print(book.author)
        return HttpResponse('This is list of books.')


class ManagerView(View):

    def get(self, request):
        employees = Employee.objects.all()
        managers = Manager.objects.all()
        managers1 = Manager.objects.filter(Q(company__icontains='com') & Q(employees__name__startswith='emp'))
        print("managers1", managers1)
        print("employees", employees)
        print("managers", managers)
        managers = Manager.objects.prefetch_related('employees')
        print("managers", managers)
        for manager in managers:
            print("employee", manager.employees.all())
        return render(request, 'index.html')


class SessionView(View):

    def post(self, request):
        request.session['username2'] = 'ashish132'
        return HttpResponse('Session data is set successfully.')

    def get(self, request):
        username = request.session.get('username2', 'guest')
        return HttpResponse(f"The username is {username}")


class AutherView(View):

    def post(self, request):

        author_obj = Author()
        author_obj.name = 'prechand'
        author_obj.save()
        return HttpResponse(f'The author {author_obj.name} is created successfully.')

    def get(self, request):

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        print("*****************")
        print("serializer_data", serializer.data)
        return HttpResponse('The list of all authors')


@receiver(post_save, sender=Author)
def send_email(sender, instance, created, **kwargs):
    print("I am sending email")
    print("sender", sender)
    print("instance", instance)
    print("created", created)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


@receiver(pre_init, sender=Author)
def access_model(sender, *args, **kwargs):
    print("Model are getting called.")
    print("sender", sender)
    print("args", args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


class PostListView(ListView):

    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):

    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'


class SraswatiView(View):

    def get(self, request):
        saraswati = SaraswariVidyaMandir.objects.select_related('school').get(id=1)
        print("saraswati", saraswati.school)
        man = Man.objects.prefetch_related('person')
        print("man", man)
        mans = Man.objects.filter(Q(name__startswith = 'a') & Q(name__icontains = 'a'))
        print("mans", mans)
        for m in man:
            print(m.person.all())
        return HttpResponse("Get sraswati vidya mandir school.")





