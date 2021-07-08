from django.db import models
from django.contrib.auth.models import User
from books.models import Books
from datetime import datetime

# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    issue_date = models.DateField(default=datetime.now, blank=True)
    return_date = models.DateField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)
