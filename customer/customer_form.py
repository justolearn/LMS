from django import forms
from books.models import Books
from .models import Customer
from datetime import date
from django.contrib.auth.models import User as user_model


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
            'issue_date': DateInput(attrs={'class': 'form-control'}),
            'return_date': DateInput(attrs={'class': 'form-control', 'readonly': True}),
            'is_returned': forms.CheckboxInput(attrs={'class': '', 'disabled': True}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields["book"].queryset = Books.objects.filter(is_available=True, available_books__gte=1)
        self.fields["user"].queryset = user_model.objects.filter(is_active=True)

    def clean(self):
        # if book is already issued and not returned restrict user to re isuue
        cleaned_data = super(CustomerForm, self).clean()
        book_id = cleaned_data["book"].id
        user_id = cleaned_data["user"].id
        queryset = Customer.objects.filter(book=book_id, user=user_id, is_returned=False)
        if queryset.exists():
            raise forms.ValidationError('Book already issued to this user ', code='invalid')
        else:
            return cleaned_data


class CustomerReturnForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'book': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'issue_date': DateInput(attrs={'class': 'form-control', 'readonly': True}),
            'return_date': DateInput(attrs={'class': 'form-control', 'value': date.today()}),
            'is_returned': forms.CheckboxInput(attrs={'class': '', 'required': True}),
        }

    def clean(self):
        # Check if total book is less that available books raise error
        cleaned_data = super(CustomerReturnForm, self).clean()
        new_count = cleaned_data["book"].available_books + 1
        if new_count <= cleaned_data["book"].total_books:
            Books.objects.update_book(cleaned_data["book"].id, available_books=new_count, is_available=True)
        else:
            raise forms.ValidationError('Available book count should be equals to total Book count ', code='invalid')
        return cleaned_data
