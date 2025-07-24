from django.urls import path
from .views import BookView, ManagerView, SaraswatiVidyaMandirView, SessionView, AuthorView,\
    PostListView, PostDetailView, TestMultipleDBView, ProductView, NotebookListCreateView, \
    NoteBookDetailView, NotebookViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title='My API',
        default_version='v1'
    ),
    public=True,
    permission_classes= (permissions.AllowAny,),
)



router = DefaultRouter()
router.register(r'copies', NotebookViewSet, basename='book')
urlpatters = router.urls



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
    path('notebooks/<int:pk>/', NoteBookDetailView.as_view(), name='NoteBookDetailView'),
]