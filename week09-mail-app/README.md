# Week 9 — Working with Mails

**Aim:** Create an application for working with mails using the Django framework.

## Project structure

```text
mail_app/
├── manage.py
├── mail_app/                  # settings (DB, email backend, auth) & root urls
├── mail/
│   ├── models.py              # Mail (sender, recipient, subject, body)
│   ├── forms.py               # MailForm, RegisterForm
│   ├── views.py               # inbox, compose, login, logout, register
│   ├── urls.py
│   └── templates/mail/
│       ├── inbox.html
│       ├── compose.html
│       ├── login.html
│       ├── register.html
│       └── logout.html
├── db.sqlite3
└── static/mail/
    ├── style.css
    └── script.js
```

## Steps

1. **Create an environment and the project:**

   ```bash
   python -m venv week9
   week9\Scripts\activate
   pip install django
   django-admin startproject mail_app
   cd mail_app
   python manage.py startapp mail
   ```

2. **Get a Gmail App Password.** Turn on 2-Step Verification for your Google account, then create one at *Google Account → Security → App passwords*. Gmail rejects your normal password over SMTP.
3. **Edit settings** in [mail_app/settings.py](open:week09-mail-app/mail_app/mail_app/settings.py): add `'mail'`, the SMTP settings with your Gmail address and App Password, the login/logout redirects, and the static folder.
4. **Write the model** in [mail/models.py](open:week09-mail-app/mail_app/mail/models.py).
5. **Write the forms** in [mail/forms.py](open:week09-mail-app/mail_app/mail/forms.py): `MailForm` (recipient, subject, body) and `RegisterForm`.
6. **Write the views** in [mail/views.py](open:week09-mail-app/mail_app/mail/views.py). `compose_view` sends the mail with `send_mail(subject, body, settings.EMAIL_HOST_USER, [recipient])` and then saves a copy in the database.
7. **Map the URLs** in [mail/urls.py](open:week09-mail-app/mail_app/mail/urls.py) (app level) and [mail_app/urls.py](open:week09-mail-app/mail_app/mail_app/urls.py) (project level).
8. **Create the templates** in `mail/templates/mail/`: [register.html](open:week09-mail-app/mail_app/mail/templates/mail/register.html), [login.html](open:week09-mail-app/mail_app/mail/templates/mail/login.html), [inbox.html](open:week09-mail-app/mail_app/mail/templates/mail/inbox.html), [compose.html](open:week09-mail-app/mail_app/mail/templates/mail/compose.html) and [logout.html](open:week09-mail-app/mail_app/mail/templates/mail/logout.html).
9. **Add the static files** [static/mail/style.css](open:week09-mail-app/mail_app/static/mail/style.css) and [static/mail/script.js](open:week09-mail-app/mail_app/static/mail/script.js) (confirm before sending, toast message, hover highlight, password show/hide).
10. **Run the application:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py collectstatic
    python manage.py runserver
    ```

    Register at http://127.0.0.1:8000/register/, then compose a mail ([screenshot](open:week09-mail-app/output/compose.jpg)). It arrives in the recipient's inbox and is listed on your Inbox page.
