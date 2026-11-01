# website/settings.py
# Only the parts you change are shown. Keep everything else that
# "django-admin startproject" generated.

# Step 6: Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

# Step 5: Configure the template directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Your custom templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Step 5: Configure the static directory
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'myapp' / 'static',
]
# (The manual also shows BASE_DIR / 'static' - use that only if you
#  make a "static" folder next to manage.py.)
