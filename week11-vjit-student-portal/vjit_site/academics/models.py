# academics/models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    description = models.TextField()
    contact_email = models.EmailField()

    def __str__(self):
        return self.name
