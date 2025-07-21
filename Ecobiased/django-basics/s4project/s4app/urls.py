from django.urls import path
from .views import BookView, ManagerView


urlpatterns = [
    path('books/', BookView.as_view(), name="books"),
    path('managers/', ManagerView.as_view(), name='managers')
]