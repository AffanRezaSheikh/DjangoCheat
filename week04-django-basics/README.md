# Week 4 — Basics of Django & Installing the Software

**Aim:** Learn the basics of the Django framework and install the required software.

## Steps

1. **Install Python** (latest version) and check it:

   ```bash
   python --version
   pip --version
   ```

   Make a parent folder for all your Django projects:

   ```bash
   mkdir my_django_project
   cd my_django_project
   ```

2. **Create and activate a virtual environment.** `venv` comes with Python, so nothing extra is needed.

   ```bash
   python -m venv week4
   week4\Scripts\activate          # Command Prompt
   week4\Scripts\Activate.ps1      # PowerShell
   ```

   Your prompt now starts with `(week4)`.
3. **Install Django** and check the version:

   ```bash
   pip install django
   django-admin --version
   ```

4. **Create the project** `website` and run it once:

   ```bash
   django-admin startproject website
   cd website
   python manage.py runserver
   ```

   Open http://127.0.0.1:8000 — the Django welcome page means Django is installed. Press `Ctrl+C` to stop.
5. **Create an app** called `myapp`:

   ```bash
   python manage.py startapp myapp
   ```

6. **Make the template and static folders** inside `myapp`:

   ```text
   website/
   ├── myapp/
   │   ├── templates/myapp/index.html
   │   └── static/myapp/
   │       ├── style.css
   │       └── script.js
   ```

   Add [index.html](open:week04-django-basics/website/myapp/templates/myapp/index.html), [style.css](open:week04-django-basics/website/myapp/static/myapp/style.css) and [script.js](open:week04-django-basics/website/myapp/static/myapp/script.js). `{% load static %}` must be the first line of the template.

   **Django templates** are HTML files with Django's own template language (DTL). They let you insert dynamic data with `{{ variable }}`, control logic with `{% tags %}` such as loops and conditionals, and extend base layouts with `{% extends %}` and `{% block %}`.
7. **Configure templates and static files** in [website/settings.py](open:week04-django-basics/website/website/settings.py): set `TEMPLATES['DIRS']`, `STATIC_URL` and `STATICFILES_DIRS`.
8. **Register the app** by adding `'myapp'` to `INSTALLED_APPS` in the same file.
9. **Write the view.** [myapp/views.py](open:week04-django-basics/website/myapp/views.py) holds view functions — they process a request and return a response (render a template, read the database, handle a form or return JSON).
10. **Map the URLs.** `urls.py` connects a URL to a view.
    - Create [myapp/urls.py](open:week04-django-basics/website/myapp/urls.py) — routes for this one app.
    - Edit [website/urls.py](open:week04-django-basics/website/website/urls.py) — the project's central dispatcher — and `include('myapp.urls')`.
11. **Run the project:**

    ```bash
    python manage.py runserver
    ```

    Open http://127.0.0.1:8000 and click **Click Me**. See [output/welcome.jpg](open:week04-django-basics/output/welcome.jpg) and [output/after-click.jpg](open:week04-django-basics/output/after-click.jpg).
