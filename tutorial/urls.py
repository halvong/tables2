from django.urls import path, re_path

from . import views

app_name = 'tutorial'

urlpatterns = [
    path('tutorial', views.PersonList.as_view(), name='person_list'),
]