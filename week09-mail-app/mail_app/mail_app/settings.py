# mail_app/settings.py
# Only the parts you change are shown. Keep everything else that
# "django-admin startproject" generated.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mail',  # our app
]

# Email backend (SMTP example: Gmail)
# Django 6.1 or newer: startproject also adds a "MAILERS = {...}" block.
# Delete that block, otherwise Django refuses to start with these EMAIL_ settings.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password_or_app_password'  # use a Gmail App Password

LOGIN_URL = '/login/'             # added: where @login_required sends users
LOGIN_REDIRECT_URL = '/inbox/'    # after login, go to inbox
LOGOUT_REDIRECT_URL = '/login/'   # after logout, go to login page

# added: the project-level static/ folder holds mail/style.css and mail/script.js
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'   # needed for "collectstatic"
