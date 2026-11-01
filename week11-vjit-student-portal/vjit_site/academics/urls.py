# academics/urls.py  (added - create this file)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
]
