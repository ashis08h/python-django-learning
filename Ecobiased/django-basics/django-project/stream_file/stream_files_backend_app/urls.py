from django.urls import path
from .views import StreamFileView

urlpatterns = [
    path('', StreamFileView.as_view(), name='stream_file_view')
]