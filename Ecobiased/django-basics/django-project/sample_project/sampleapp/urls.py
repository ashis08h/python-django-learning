from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BookView.as_view(), name='BookView'),
    path('managers', views.ManagerView.as_view(), name='ManagerView'),
    path('set_session', views.SessionView.as_view(), name='SessionView'),
    path('get_session', views.SessionView.as_view(), name='SessionView'),
    path('author/create', views.AutherView.as_view(), name='AuthorView'),
    path('post/list', views.PostListView.as_view(), name='PostListView'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='PostDetailView'),
    path('saraswati', views.SraswatiView.as_view(), name='SaraswatiVidyaMandir')

]