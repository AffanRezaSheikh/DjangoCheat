# shopping_cart/settings.py
# Only the parts you change are shown. Keep everything else that
# "django-admin startproject" generated.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
]

LOGIN_URL = 'login'              # added: where @login_required sends users
LOGIN_REDIRECT_URL = 'catalog'
LOGOUT_REDIRECT_URL = 'login'
