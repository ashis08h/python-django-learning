from django.urls import path
from .views import BookView, ManagerView, SessionView, AuthorView, PostListView, PostDetailView, SaraswatiView


urlpatterns = [
    path('books', BookView.as_view(), name='Book_list'),
    path('managers', ManagerView.as_view(), name='manager_list'),
    path('session', SessionView.as_view(), name='session'),
    path('author', AuthorView.as_view(), name='author'),
    path('posts', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('saraswati', SaraswatiView.as_view(), name='saraswati')
]