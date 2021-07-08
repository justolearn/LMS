from rest_framework import serializers
from django.contrib.auth.models import User as user_model
from .models import Customer
from books.serializers import BooksSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    book = BooksSerializer(read_only=True, many=True)
    class Meta:
        model = Customer
        fields = '__all__'
