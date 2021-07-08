from django import forms
from django.contrib.auth.models import User as user_model

from customer.models import Customer


class UserForm(forms.ModelForm):
    # username = forms.CharField(max_length=100, required=True)
    # first_name = forms.CharField(max_length=200, required=False)
    # last_name = forms.CharField(max_length=200, required=False)
    # email = forms.EmailField(help_text='A valid email address.', required=False)
    # password = forms.CharField(widget=forms.PasswordInput())
    #
    # active = forms.BooleanField()

    # def __init__(self):
    #     self.fields['active'].initial = True

    class Meta:
        model = user_model
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'is_active',)
        # fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs= {'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': ''}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     id = kwargs['instance'].id
    #     self.fields["issued_book"] = Customer.objects.filter(id=id)
    #     print(self)

