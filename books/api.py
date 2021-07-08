from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from books.book_form import BookForm
from books.models import Books, Genre, Author


def book_list(request):
    try:
        queryset = Books.objects.all()
        return render(request, 'books/book_listing.html', {'book_list': queryset, "book_page": "active"})
    except Exception as e:
        print('Excepion ', e)


class AddBook(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'books/add_book.html'

    def get_success_url(self):
        return reverse('book_list', kwargs={})


class DeleteBook(DeleteView):
    model = Books
    form_class = BookForm
    template_name = 'books/delete_book.html'

    def get_success_url(self):
        return reverse('book_list', kwargs={})


class UpdateBook(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'books/update_book.html'

    def get_success_url(self):
        return reverse('book_list', kwargs={})





