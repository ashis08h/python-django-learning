from django.shortcuts import render
from django.views import View
from .models import Book, Post, School, SaraswatiVidyaMandir, Person, Employee,\
                     Manager, Man, Woman, Author, Product, NoteBook
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from .serializers import AuthorSerializer, NoteBookSerializer
from django.views.generic import ListView, DetailView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .tasks import add
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from rest_framework import filters


# Create your views here.

class BookView(View):

    def get(self, request):
        authors = Author.objects.all()
        books = Book.objects.all()
        print("authors", authors)
        print("books", books)
        # return HttpResponse("I am from BookView get method.")
        author1 = list(Book.objects.filter(id=1).values('author'))
        print('author1', author1)
        book = Book.objects.select_related('author').get(id=1)
        print('book', book)
        return render(request, 'book.html', context={'authors': authors})


class ManagerView(View):

    def get(self, request):
        employees = Employee.objects.all()
        managers = Manager.objects.all()
        print("managers", managers)
        print("employees", employees)
        manager = Manager.objects.filter(Q(company__icontains='man') & (Q(employees__name__startswith='emp')))
        print('manager', manager)
        manager_list = Manager.objects.prefetch_related('employees')
        print('employees_list', manager_list)
        for manager in manager_list:
            print("emloyees_list", manager.employees.all())
        return render(request, 'manager.html', context={'employees': employees})


class SaraswatiVidyaMandirView(View):

    def get(self, request):
        saraswati_vidya_mandir = SaraswatiVidyaMandir.objects.select_related('school').get(id=1)
        print("saraswati_vidya_mandir", saraswati_vidya_mandir)
        mans = Man.objects.prefetch_related('persons')
        print("mans", mans)
        for man in mans:
            print(man.persons.all())
        mans1 = Man.objects.filter(Q(name__icontains='m') & Q(name__startswith='ma'))
        print("mans1", mans1)
        return render(request, 'school.html', context={'school': saraswati_vidya_mandir.school})


class SessionView(View):

    def get(self, request):
        request.session['username1'] = 'Ashish Kumar sah'
        print("username from session is ", request.session.get("username1", None))
        return HttpResponse("I am from Session View.")


@receiver(post_save, sender=Author)
def send_email(sender, instance, created, **kwargs):
    print("I am from send email")
    print("sender", sender)
    print("instance", instance)
    print("created", created)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


@receiver(pre_init, sender=Author)
def access_model(sender, *args, **kwargs):
    print("I am from access model.")
    print("sender", sender)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


class AuthorView(View):
    def post(self, request):
        author = Author()
        author.name = 'CustomAuthor'
        author.save()
        return HttpResponse('Author created successfully.')

    def get(self, request):
        authors = Author.objects.all()
        authorserializer = AuthorSerializer(authors, many=True)
        print("serializer", authorserializer.data)
        return render(request, 'author.html', context={'authors': authorserializer.data})


class PostListView(ListView):

    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class TestMultipleDbView(View):

    def get(self, request):
        post = Post.objects.all().using('new')
        print('post', post)
        return HttpResponse("I am from multipledbclass.")


class ProductView(View):

    def get(self, request):
        plain_password = "Ashish"
        hashed_password = make_password(plain_password)
        print("hashed_password", hashed_password)
        try:
            user = User.objects.get(username = 'ashish')
            is_correct_password = user.check_password('ashish1')
            print("is_correct_password", is_correct_password)
        except:
            user = None
        print(user)
        result = add.delay(2, 4)
        print("result_id", result.id)
        return render(request, 'product.html')

    def post(self, request):
        name = request.POST.get('name')
        desc = request.POST.get('description')
        product = Product()
        product.name = name
        product.description = desc
        product.full_clean()
        product.save()
        return HttpResponse("sucessfully submitted the records.")


class NoteBookListCreateView(generics.ListCreateAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer
    # adding permission_class then we need to register authentication in settings.py file.
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['published_date']


class NoteBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer
    permission_classes = [IsAdminOrReadOnly]


class NoteBookViewSet(viewsets.ModelViewSet):
    """
    We need to use viewsets for more complex apis.
    """
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer







