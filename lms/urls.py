from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# from rest_framework import routers
from books.views import BooksViewSet, GenreViewSet, AuthorViewSet
from customer.views import UserViewSet
from customer.urls import urlpatterns as user_urls
from .view import home

schema_view = get_swagger_view(title='Pastebin API')
# router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'customer', UserViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
                  path('', home),
                  path('admin/', admin.site.urls),
                  path('book/', include('books.urls')),
                  path('user/', include(user_urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('swagger/', schema_view),
                  path('api/', include(router.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

