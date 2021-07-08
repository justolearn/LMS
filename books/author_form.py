from django import forms
from .models import Author


class DateInput(forms.DateInput):
    input_type = 'date'


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs= {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'total_books': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control'}),
            'date_of_death': DateInput(attrs={'class': 'form-control'}),
        }

