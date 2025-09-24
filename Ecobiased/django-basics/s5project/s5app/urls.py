from django.urls import path
from .views import BookView, ManagerView, SaraswatiVidyaMandirView, SessionView, AuthorView, PostListView,\
    PostDetailView, TestMultipleDBView, ProductView, NoteBookListCreateView, NotebookViewSet, NoteBookDetailView
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


shema_view = get_schema_view(
    openapi.Info(
        title='My API',
        default_version='v1'
    ),
    public=True,
    permission_classes= (permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'copies', NotebookViewSet, basename='book')
urlpatterns = router.urls

urlpatterns = [
    path('books/', BookView.as_view(), name='books'),
    path('managers/', ManagerView.as_view(), name='managers'),
    path('saraswati_vidya_mandir/', SaraswatiVidyaMandirView.as_view(), name='saraswati_vidya_mandir'),
    path('session/', SessionView.as_view(), name="session"),
    path('authors/', AuthorView.as_view(), name='author'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('multiple_db_posts/', TestMultipleDBView.as_view(), name='test_multiple_db'),
    path('products/', ProductView.as_view(), name='products'),
    path('notebooks/', NoteBookListCreateView.as_view(), name='notebooklistcreate'),
    path('notebook/<int:pk>/', NoteBookDetailView.as_view(), name='notebook_detail_view')

]