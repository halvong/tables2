import datetime
from django.contrib.auth import get_user_model
from django.db import models

class Person(models.Model):
    first_name = models.CharField(default='', blank=True, max_length=200)
    last_name = models.CharField(default='', blank=True, max_length=200)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    birth_date = models.DateField(default=datetime.date, null=True, blank=True)