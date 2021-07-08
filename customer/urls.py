# from .views import UserTemplateViewSet
from django.urls import path
from .api import user_list, user_detail, AddUser, DeleteUser, UpdateUser
from .customer_api import IssueBook, issue_list, ReturnBook

urlpatterns = [
    path('user_list/', user_list, name='user_list'),
    path('add_user/', AddUser.as_view(), name='add_user'),
    path('delete_user/<pk>/', DeleteUser.as_view(), name='delete_user'),
    path('update_user/<pk>/', UpdateUser.as_view(), name='update_user'),
    path('user_detail/<int:user_id>', user_detail, name='user_detail'),
    #     issue book
    path('issue_list/', issue_list, name='issue_list'),
    path('issue_book/', IssueBook.as_view(), name='issue_book'),
    path('return_book/<pk>/', ReturnBook.as_view(), name='return_book'),
]
