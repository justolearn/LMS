from django.db.models import Q
from django.db import models


class BooksQuerySet(models.QuerySet):
    def by_genre_id(self, genre_id):
        """
        Queryset to get books by genre
        :param id: int
        :return: List of books Objects
        """

        return self.filter(genre=genre_id)

    def by_author_id(self, author_id):
        return self.filter(author=author_id)

    def by_genre_name(self, genre):
        return self.filter(genre__name__icontains=genre)

    def by_auth_gen(self, author, genre):
        return self.filter(Q(author__first_name__icontains=author) | Q(author__last_name__icontains=author),
                           genre__name__icontains=genre)

    def update_book(self, update_id, **update_data):
        return self.filter(id=update_id).update(**update_data)