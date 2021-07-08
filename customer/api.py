from django.contrib.auth.models import User as user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .user_form import UserForm


# from django.template import loader
# from django.http import HttpResponse


def user_list(request):
    try:
        queryset = user_model.objects.all()
        return render(request, 'user/user_list.html', {'user_list': queryset, "user_page": "active"})
    except Exception as e:
        print('Excepion ', e)


def user_detail(request, user_id):
    try:
        queryset = get_object_or_404(user_model, id=user_id)
        return render(request, 'user/user_detail.html', {'user':  queryset})
    except Exception as e:
        print('Excepion ', e)


class AddUser(CreateView):
    model = user_model
    form_class = UserForm
    template_name = 'user/add_user.html'

    def get_success_url(self):
        return reverse('user_list', kwargs={})


class DeleteUser(DeleteView):
    model = user_model
    form_class = UserForm
    template_name = 'user/delete_user.html'

    def get_success_url(self):
        return reverse('user_list', kwargs={})


class UpdateUser(UpdateView):
    model = user_model
    form_class = UserForm
    template_name = 'user/update_user.html'

    def get_success_url(self):
        return reverse('user_list', kwargs={})


