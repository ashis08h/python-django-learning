from django.shortcuts import render
from django.views import View
from s3app.models import Author, Book, Employee, Manager, SaraswatiVidyaMandir, Man, Post,\
    Product, NoteBook
from django.http import HttpResponse
from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_init
from s3app.serializers import AuthorSerializer, NoteBookSerializer
from django.views.generic import ListView, DetailView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from s3app.tasks import add
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from s3app.permissions import IsAdminOrReadOnly

# Create your views here.


class BookView(View):

    def get(self, request):
        authors = Author.objects.all()
        books = Book.objects.all()
        print("authors", authors)
        print("books", books)
        # return HttpResponse("I am from get method of BookView class.")

        author1 = Author.objects.filter(id=1)
        #print("author1", author1)
        book = Book.objects.select_related('author').get(id=1)
        #print("book", book)
        books = list(Book.objects.filter(id=1).values('author'))
        books = list(Book.objects.filter(id=1).values_list('author'))
        print("books", books)
        return render(request, 'book.html', context={'author': authors})


class ManagerView(View):

    def get(self, request):
        employees = Employee.objects.all()
        managers = Manager.objects.all()
        # print("managers", managers)
        # print("employees", employees)
        manager = Manager.objects.filter(Q(company__icontains='comp') & Q(employee__name__startswith='emp'))
        # print("manager", manager)
        manager_list = Manager.objects.prefetch_related('employee')
        # print("manager_list", manager_list)
        for manager in manager_list:
            print(manager.employee.all())
        return render(request, 'manager.html', context={'managers': managers})


class SaraswatiVidyaMandirView(View):

    def get(self, request):
        saraswati_vidya_mandir = SaraswatiVidyaMandir.objects.select_related('school').get(id=1)
        print("saraswati_vidya_mandir", saraswati_vidya_mandir)
        mans = Man.objects.prefetch_related('person')
        print("mans", mans)
        for man in mans:
            print(man.person.all())
        mans = Man.objects.filter(Q(name__icontains='m') & Q(name__startswith='ma'))
        return render(request, 'saraswati_vidya_mandir.html', context={'mans':mans})


class SessionView(View):

    def get(self, request):
        request.session['username'] = 'Ashish Kumar'
        print(f"I Have stored the session with name {request.session.get('username', None)}")
        return HttpResponse(f"I am from SessionView, and my session is {request.session.get('username', None)}")


@receiver(post_save, sender=Author)
def send_email(sender, instance, created, **kwargs):
    print("I am from sender email function.")
    print("sender", sender)
    print("instance", instance)
    print("created", created)
    for key, value in kwargs.items():
        print(f"{key}:{value}")


@receiver(pre_init, sender=Author)
def access_model(sender, *args, **kwargs):
    print("I am from access_model")
    print("sender", sender)
    for key, value in kwargs.items():
        print(f"{key}:{value}")


class AuthorView(View):

    def post(self, request):
        author_obj = Author()
        author_obj.name = 'Custom_author'
        author_obj.save()
        return HttpResponse("Author entry created successfully.")

    def get(self, request):

        authors = Author.objects.all()
        author_serializers = AuthorSerializer(authors, many=True)
        print('author_serializers', author_serializers.data)
        return render(request, 'author.html', context={'authors': author_serializers.data})


class PostListView(ListView):

    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class TestMultipleDbView(View):

    def get(self, request):
        posts = Post.objects.all().using('new_database')
        print('posts', posts)
        return HttpResponse("I am from Multipledbview")


class ProductView(View):

    def get(self, request):
        plain_password = 'Ashish'
        hashed_password = make_password(plain_password)
        print("hashed_password", hashed_password)
        try:
            user_obj = User.objects.get(username='ashish')
            is_correct_password = user_obj.check_password('ashish')
            print("is_correct_password", is_correct_password)
        except:
            user_obj = None
        print("user", user_obj)
        #result = add.delay(2, 3)
        #print("result_id", result.id)
        return render(request, 'product.html')

    def post(self, request):
        name = request.POST.get('name')
        desc = request.POST.get('description')
        product = Product()
        product.name = name
        product.desc  = desc
        product.full_clean()
        product.save()
        return HttpResponse('Successfully submitted the records.')


class NoteBookListCreateView(generics.ListCreateAPIView):

    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer
    # Adding permissions class then we need to register authentication in settings.py file.
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['published_date']


class NoteBookViewSet(viewsets.ModelViewSet):

    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer


class NoteBookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer
    permission_classes = [IsAdminOrReadOnly]





