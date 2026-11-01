# Week 11 — Case Study: VJIT Student Portal, Deployed to GitHub

**Aim:** Build a Django application for the VJIT Student Portal and deploy it to GitHub.

## Apps in the portal

| App | Holds |
|---|---|
| `main` | Homepage, About, Contact |
| `academics` | Departments, Courses |
| `admissions` | Admission info, forms |
| `events` | News, Events, Announcements |
| `students` | Student portal, results, notices |

The manual builds `main` and `academics`; the other three follow the same pattern.

## Step 1 — Build the site

1. **Create the project and apps:**

   ```bash
   python -m venv week11
   week11\Scripts\activate
   pip install django
   django-admin startproject vjit_site
   cd vjit_site
   python manage.py startapp main
   python manage.py startapp academics
   ```

2. **Register the apps** in [vjit_site/settings.py](open:week11-vjit-student-portal/vjit_site/vjit_site/settings.py).
3. **Write the model** [academics/models.py](open:week11-vjit-student-portal/vjit_site/academics/models.py) (`Department`) and register it in [academics/admin.py](open:week11-vjit-student-portal/vjit_site/academics/admin.py).
4. **Write the home view** [main/views.py](open:week11-vjit-student-portal/vjit_site/main/views.py) and its template [main/templates/main/home.html](open:week11-vjit-student-portal/vjit_site/main/templates/main/home.html).
5. **Add the academics page** — [academics/views.py](open:week11-vjit-student-portal/vjit_site/academics/views.py), [academics/urls.py](open:week11-vjit-student-portal/vjit_site/academics/urls.py) and [department_list.html](open:week11-vjit-student-portal/vjit_site/academics/templates/academics/department_list.html).
6. **Map the project URLs** in [vjit_site/urls.py](open:week11-vjit-student-portal/vjit_site/vjit_site/urls.py).
7. **Run it:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

## Step 2 — Put the project on GitHub

1. **Create a GitHub account** and install Git (`git --version` to check).
2. **Save your packages and ignore local files:**

   ```bash
   pip install gunicorn
   pip freeze > requirements.txt
   ```

   Add a [.gitignore](open:week11-vjit-student-portal/vjit_site/.gitignore) so `venv/`, `db.sqlite3` and `.env` are not uploaded. A minimal [requirements.txt](open:week11-vjit-student-portal/vjit_site/requirements.txt) is shown too.
3. **Commit locally:**

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Create a repository on GitHub** — click *New repository*, name it (e.g. `vjit-app`), choose Public or Private, and do not add a README.
5. **Link and push:**

   ```bash
   git remote add origin https://github.com/your-username/vjit-app.git
   git branch -M main
   git push -u origin main
   ```

## Step 3 — Hosting

**GitHub Pages** only hosts static HTML/CSS/JS. For a static site: push the code, go to *Settings → Pages*, choose branch `main` and folder `/ (root)` or `/docs`, and save. GitHub gives you a URL like `https://your-username.github.io/vjit-app/`.

**GitHub cannot run Django** — Django needs Python and a server. Use a Python host such as PythonAnywhere or Render.

**Deploy with Render:**

1. Push the project to GitHub (Step 2).
2. Sign in at render.com and create a new **Web Service** connected to your repository.
3. **Build Command:** `pip install -r requirements.txt && python manage.py migrate`
4. **Start Command:** `gunicorn vjit_site.wsgi:application`
5. Add environment variables (for example `PYTHON_VERSION`), and add `'.onrender.com'` to `ALLOWED_HOSTS`.
6. Deploy — Render gives you a live URL such as `https://vjit-django.onrender.com`.
