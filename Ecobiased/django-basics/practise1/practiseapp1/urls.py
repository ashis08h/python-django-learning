from django.urls import path
from .views import BookView, ManagerView, SaraswatiVidyaMandirView, SessionView, AuthorView,\
                    PostListView, PostDetailView


urlpatterns = [
    path('book', BookView.as_view(), name="bookview"),
    path('manager', ManagerView.as_view(), name="managerview"),
    path('saraswati_vidya_mandir', SaraswatiVidyaMandirView.as_view(), name='saraswati_vidya_mandir'),
    path('session', SessionView.as_view(), name='session_view'),
    path('author', AuthorView.as_view(), name="auther_view"),
    path('posts', PostListView.as_view(), name='post_view'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_delete_view'),
]