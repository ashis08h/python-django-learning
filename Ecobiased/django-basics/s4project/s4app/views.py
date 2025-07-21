from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from .models import Author, Book, Employee, Manager

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


