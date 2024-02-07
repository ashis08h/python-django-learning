from django.urls import path
from .views import BookView, ManagerView, SessionView, AuthorView


urlpatterns = [
    path('books', BookView.as_view(), name='Book_list'),
    path('managers', ManagerView.as_view(), name='manager_list'),
    path('session', SessionView.as_view(), name='session'),
    path('author', AuthorView.as_view(), name='author')
]