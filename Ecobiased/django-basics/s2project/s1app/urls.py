from django.urls import path
from .views import BookView, ManagerView, SaraswatiVidyaMandirView,\
    SessionView, AuthorView, PostListView, PostDetailView, TestMultipleDbView, ProductView,\
    NoteBookListCreateView, NoteBookDetailView, NoteBookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
    ),
    public=True,
    permission_classes = (permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'copies', NoteBookViewSet, basename='book')
urlpatterns = router.urls

urlpatterns = [
    path('books', BookView.as_view(), name='books'),
    path('managers', ManagerView.as_view(), name='manager'),
    path('school', SaraswatiVidyaMandirView.as_view(), name='school'),
    path('get_or_set_session', SessionView.as_view(), name='get_or_session'),
    path('authors', AuthorView.as_view(), name='authorview'),
    path('posts', PostListView.as_view(), name='postlistview'),
    path('post/<int:pk>', PostDetailView.as_view(), name='postdetailview'),
    path('multiple', TestMultipleDbView.as_view(), name='multiple'),
    path('product', ProductView.as_view(), name='product'),
    path('notebooks', NoteBookListCreateView.as_view(), name='notebook-list'),
    path('notebook/<int:pk>', NoteBookDetailView.as_view(), name='book-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

