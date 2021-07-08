from rest_framework import serializers
from .models import Books, Genre, Author


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['first_name']


class BooksSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Books
        fields = '__all__'
