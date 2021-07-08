from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from books.author_form import AuthorForm
from books.models import Author


def author_list(request):
    try:
        queryset = Author.objects.all()
        return render(request, 'author/author_listing.html', {'author_list': queryset, "author_page": "active"})
    except Exception as e:
        print('Excepion ', e)


class AddAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/add_author.html'

    def get_success_url(self):
        return reverse('author_list', kwargs={})


class DeleteAuthor(DeleteView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/delete_author.html'

    def get_success_url(self):
        return reverse('author_list', kwargs={})


class UpdateAuthor(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/update_author.html'

    def get_success_url(self):
        return reverse('author_list', kwargs={})





