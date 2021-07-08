from books.models import Books
from .models import Customer
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from .customer_form import CustomerForm, CustomerReturnForm


def issue_list(request):
    try:
        queryset = Customer.objects.all().order_by('is_returned')
        return render(request, 'customer/issue_list.html', {'issue_list': queryset, "library_page": "active"})
    except Exception as e:
        print('Excepion ', e)


class IssueBook(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/issue_book.html'

    def get_success_url(self):
        return reverse('issue_list', kwargs={})

    def form_valid(self, form):
        if form.cleaned_data["book"].available_books > 0:
            new_count = form.cleaned_data["book"].available_books - 1
            if new_count != 0:
                Books.objects.update_book(form.cleaned_data["book"].id, available_books=new_count, is_available=True)
                # Books.objects.filter(id=form.cleaned_data["book"].id) \
                #     .update(available_books=new_count, is_available=True)
            if new_count == 0:
                Books.objects.update_book(form.cleaned_data["book"].id, available_books=new_count, is_available=False)
            return super().form_valid(form)


class ReturnBook(UpdateView):
    model = Customer
    form_class = CustomerReturnForm
    template_name = 'customer/return_book.html'

    def get_success_url(self):
        return reverse('issue_list', kwargs={})
