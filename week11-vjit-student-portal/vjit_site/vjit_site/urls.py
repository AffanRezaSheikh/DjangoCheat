# vjit_site/urls.py  (project level url mapping)
from django.contrib import admin
from django.urls import path, include
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('academics/', include('academics.urls')),
]
