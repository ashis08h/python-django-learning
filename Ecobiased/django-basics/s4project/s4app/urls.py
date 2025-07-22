from django.urls import path
from .views import BookView, ManagerView, SaraswatiVidyaMandirView, SessionView, AuthorView


urlpatterns = [
    path('books/', BookView.as_view(), name="books"),
    path('managers/', ManagerView.as_view(), name='managers'),
    path('svm/', SaraswatiVidyaMandirView.as_view(), name="saraswati_vidya_mandir"),
    path('session/', SessionView.as_view(), name='session'),
    path('author/', AuthorView.as_view(), name='author')
]