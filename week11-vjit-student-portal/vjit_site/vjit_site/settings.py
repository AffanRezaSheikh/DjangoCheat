# vjit_site/settings.py
# Only the parts you change are shown. Keep everything else that
# "django-admin startproject" generated.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'academics',
]

# For deployment on Render, also allow its domain:
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']
