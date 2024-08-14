from django.urls import path
from .views import BookView, ManagerView, SaraswatiVidyaMandirView,\
    SessionView

urlpatterns = [
    path('books', BookView.as_view(), name='books'),
    path('managers', ManagerView.as_view(), name='manager'),
    path('school', SaraswatiVidyaMandirView.as_view(), name='school'),
    path('get_or_set_session', SessionView.as_view(), name='get_or_session')
]