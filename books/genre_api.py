from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from books.genre_form import GenreForm
from books.models import Genre


def genre_list(request):
    try:
        queryset = Genre.objects.all()
        return render(request, 'genre/genre_listing.html', {'genre_list': queryset, "genre_page": "active"})
    except Exception as e:
        print('Excepion ', e)


class AddGenre(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/add_genre.html'

    def get_success_url(self):
        return reverse('genre_list', kwargs={})


class DeleteGenre(DeleteView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/delete_genre.html'

    def get_success_url(self):
        return reverse('genre_list', kwargs={})


class UpdateGenre(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/update_genre.html'

    def get_success_url(self):
        return reverse('genre_list', kwargs={})





