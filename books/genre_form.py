from django import forms
from .models import Genre


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control'})
        }
