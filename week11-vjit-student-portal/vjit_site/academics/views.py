# academics/views.py
# added: the project urls.py includes 'academics.urls', so the app needs
# at least one view. This one lists the departments added in admin.
from django.shortcuts import render
from .models import Department

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'academics/department_list.html', {'departments': departments})
