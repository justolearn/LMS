from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .managers import BooksQuerySet

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=500, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=500)
    pages = models.IntegerField()
    genre = models.ManyToManyField(Genre, related_name='genre')
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    photo_main = models.ImageField(upload_to='photos/books/', blank=True)
    is_available = models.BooleanField(default=True)
    total_books = models.IntegerField(blank=True, null=True)
    available_books = models.IntegerField(blank=True, null=True)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)

    objects = BooksQuerySet.as_manager()

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name} by {self.author}'

    def clean(self):
        if self.total_books < self.available_books:
            raise ValidationError({'available_books': 'Available books cannot be greater than total books'}, code='invalid')

    # def clean(self):
    #     # Don't allow draft entries to have a pub_date.
    #     if self.available_books > self.total_books:
    #         raise ValidationError(_('Draft entries may not have a publication date.'))


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/author/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
