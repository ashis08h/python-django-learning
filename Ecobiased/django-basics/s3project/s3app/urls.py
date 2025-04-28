from django.urls import path
from s3app.views import BookView, ManagerView, SaraswatiVidyaMandirView, SessionView\
    ,AuthorView, PostListView, PostDetailView, TestMultipleDbView, ProductView,\
    NoteBookListCreateView, NoteBookViewSet, NoteBookDetailView
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='My API',
        default_version='v1'
    ),
    public=True,
    permission_classes= (permissions.AllowAny,),
)
router = DefaultRouter()
router.register(r'copies', NoteBookViewSet, basename='book')
urlpatterns = router.urls

urlpatterns = [
    path('books', BookView.as_view(), name="books"),
    path('managers', ManagerView.as_view(), name='managers'),
    path('saraswati', SaraswatiVidyaMandirView.as_view(), name='saraswati'),
    path('session', SessionView.as_view(), name='session'),
    path('author', AuthorView.as_view(), name='author'),
    path('posts', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('test_multiple_db', TestMultipleDbView.as_view(), name='test_multiple'),
    path('product', ProductView.as_view(), name='product'),
    path('notebooks', NoteBookListCreateView.as_view(), name='notebook_list'),
    path('notebook/<int:pk>', NoteBookDetailView.as_view(), name='notebook_list'),
]