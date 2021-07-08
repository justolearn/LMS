from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from .views import display_all_books


# urlpatterns = [
#     # path('display_all_books/', display_all_books),
# ]

# from rest_framework.routers import DefaultRouter
# from .views import BooksViewSet
#
# router = DefaultRouter()
# router.register(r'', BooksViewSet)
# urlpatterns = router.urls
from books.api import book_list, AddBook, DeleteBook, UpdateBook
from books.genre_api import AddGenre, DeleteGenre, UpdateGenre, genre_list
from books.author_api import AddAuthor, DeleteAuthor, UpdateAuthor, author_list

urlpatterns = [
    # book urls
    path('add_book/', AddBook.as_view(), name='add_book'),
    path('book_list/', book_list, name='book_list'),
    path('delete_book/<pk>/', DeleteBook.as_view(), name='delete_book'),
    path('update_book/<pk>/', UpdateBook.as_view(), name='update_book'),
    # Genre urlpatterns
    path('add_genre/', AddGenre.as_view(), name='add_genre'),
    path('genre_list/', genre_list, name='genre_list'),
    path('delete_genre/<pk>/', DeleteGenre.as_view(), name='delete_genre'),
    path('update_genre/<pk>/', UpdateGenre.as_view(), name='update_genre'),
    # Author urlpatterns
    path('add_author/', AddAuthor.as_view(), name='add_author'),
    path('author_list/', author_list, name='author_list'),
    path('delete_author/<pk>/', DeleteAuthor.as_view(), name='delete_author'),
    path('update_author/<pk>/', UpdateAuthor.as_view(), name='update_author'),
]
