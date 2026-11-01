# weather/urls.py  (app level - create this file)
from django.urls import path
from .views import dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
]
