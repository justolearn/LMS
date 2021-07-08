from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Books, Genre, Author
from django.http import HttpResponse
from .serializers import BooksSerializer, GenreSerializer, AuthorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Books.objects.all().order_by('-date_joined')
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Books.objects.all().order_by('-date_joined')
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class BooksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Books.objects.all().order_by('-date_joined')
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['GET'])
    def by_genre(self, request, pk=None):
        try:
            queryset = Books.objects.by_genre_id(pk)

            serializer = BooksSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            print('Excepion ', e)

    @action(detail=True, methods=['GET'])
    def by_author(self, request, pk=None):
        try:
            queryset = Books.objects.by_author_id(pk)

            serializer = BooksSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            print('Excepion ', e)

    @action(detail=False, methods=['GET'], url_path='by_genre_name/(?P<genre>[^/.]+)')
    def by_genre_name(self, request, genre):
        try:
            queryset = Books.objects.by_genre_name(genre)

            serializer = BooksSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            print('Excepion ', e)

    @action(detail=False, methods=['GET'], url_path='by_auth_gen')
    def by_auth_gen(self, request):
        try:
            print('**** ', self.request.query_params.get('genre'))
            print('**** ', self.request.query_params.get('author'))
            genre = self.request.query_params['genre']
            author = self.request.query_params['author']
            # queryset = Books.objects.filter(genre__name__icontains=genre, author__first_name__icontains=author)
            queryset = Books.objects.by_auth_gen(author, genre)
            serializer = BooksSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            print('Exception ', e)



from django.shortcuts import render

# Create your views here.



# def display_all_books(request):
#     books = Books.objects.all()
#     return HttpResponse(books)


from django.core import serializers


# def display_all_books(request):
#     books = Books.objects.all()
#     book_list = serializers.serialize('json', books)
#     return HttpResponse(book_list)


# def display_all_books(request):
#     books = Books.objects.all()
#     book_list = serializers.serialize('json', books)
#     return HttpResponse(book_list, content_type="text/json-comment-filtered")


# def display_all_books(request):
#     books = Books.genre.through.objects.all()
#     book_list = serializers.serialize('json', books)
#     return HttpResponse(book_list, content_type="text/json-comment-filtered")

