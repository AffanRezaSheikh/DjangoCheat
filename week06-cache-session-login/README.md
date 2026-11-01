# Week 6 — Cache & Session Management for Student Login

**Aim:** Demonstrate cache and session management for a student login application.

## Project structure

```text
student_login_project/
├── manage.py
├── student_login_project/
│   ├── settings.py        # cache + session settings
│   └── urls.py            # project-level routing
├── studentlogin/
│   ├── admin.py           # register Student model
│   ├── models.py          # Student model (username, password)
│   ├── views.py           # login, logout, dashboard (cache + session + cookie)
│   ├── urls.py            # app routes
│   └── templates/
│       ├── login.html
│       └── dashboard.html
└── db.sqlite3
```

## Steps

1. **Create an environment:**

   ```bash
   python -m venv week6
   week6\Scripts\activate
   pip install django
   ```

2. **Create the project** `student_login_project`:

   ```bash
   django-admin startproject student_login_project
   cd student_login_project
   ```

3. **Create the app** `studentlogin`:

   ```bash
   python manage.py startapp studentlogin
   ```

4. **Configure settings** in [student_login_project/settings.py](open:week06-cache-session-login/student_login_project/student_login_project/settings.py): add the app, set `TEMPLATES`, add the `CACHES` block (`LocMemCache`) and `SESSION_ENGINE` (database-backed sessions).
5. **Create the model** in [studentlogin/models.py](open:week06-cache-session-login/student_login_project/studentlogin/models.py). `save()` hashes the password with `make_password`; `check_password()` compares a typed password with the hash.
6. **Register the model** in [studentlogin/admin.py](open:week06-cache-session-login/student_login_project/studentlogin/admin.py).
7. **Write the views** in [studentlogin/views.py](open:week06-cache-session-login/student_login_project/studentlogin/views.py). `login_view` shows all three techniques:
   1. **Cache** — `cache.get(username)` first; on a miss, read the database and `cache.set(username, student, timeout=300)`.
   2. **Session** — store `student_id` and `username` in `request.session`.
   3. **Cookie** — `response.set_cookie("student_username", ..., max_age=3600)`.

   `logout_view` calls `request.session.flush()` and `response.delete_cookie(...)`.
8. **Map the URLs** in [studentlogin/urls.py](open:week06-cache-session-login/student_login_project/studentlogin/urls.py) (app level) and [student_login_project/urls.py](open:week06-cache-session-login/student_login_project/student_login_project/urls.py) (project level).
9. **Create the templates** in `studentlogin/templates/`: [login.html](open:week06-cache-session-login/student_login_project/studentlogin/templates/login.html) and [dashboard.html](open:week06-cache-session-login/student_login_project/studentlogin/templates/dashboard.html).
10. **Migrate, create an admin and run:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```

11. **Test it.** Add a student at http://127.0.0.1:8000/admin/, log in at `/login/`, open `/dashboard/`, then `/logout/`. In the browser press `F12` → *Application* → *Cookies* to watch `sessionid` and `student_username` appear and disappear ([dashboard](open:week06-cache-session-login/output/dashboard-cookie.jpg), [logout](open:week06-cache-session-login/output/logout-cookie.jpg)).
