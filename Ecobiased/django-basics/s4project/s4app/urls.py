from django.urls import path
from .views import BookView, ManagerView, SaraswatiVidyaMandirView, SessionView, AuthorView,\
    PostListView, PostDetailView, TestMultipleDBView, ProductView, NotebookListCreateView, \
    NoteBookDetailView, NotebookViewSet


urlpatterns = [
    path('books/', BookView.as_view(), name="books"),
    path('managers/', ManagerView.as_view(), name='managers'),
    path('svm/', SaraswatiVidyaMandirView.as_view(), name="saraswati_vidya_mandir"),
    path('session/', SessionView.as_view(), name='session'),
    path('author/', AuthorView.as_view(), name='author'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('test-multidb/', TestMultipleDBView.as_view(), name='multidb'),
    path('products/', ProductView.as_view(), name='products'),
    path('notebooks/', NotebookListCreateView.as_view(), name='notebooks'),
    # path('notebookviewset/', NotebookViewSet.as_view(), name='notebookviewset'),
    # path('NoteBookDetailView/', NoteBookDetailView.as_view(), name='NoteBookDetailView'),
]