from django.contrib import admin
from .models import Books, Genre, Author

# Register your models here.

admin.site.register(Books)
admin.site.register(Genre)
admin.site.register(Author)
