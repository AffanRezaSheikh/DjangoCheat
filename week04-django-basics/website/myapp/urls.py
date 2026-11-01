# myapp/urls.py  (create this file - startapp does not make it)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
