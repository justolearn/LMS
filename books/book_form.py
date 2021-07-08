from django import forms
from .models import Books


class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'genre': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'photo_main': forms.FileInput(attrs={'class': 'form-control'}),
            'total_books': forms.NumberInput(attrs={'class': 'form-control'}),
            'available_books': forms.NumberInput(attrs={'class': 'form-control'}),
            'publish_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
