# Week 7 — Quiz Application with SQLite3

**Aim:** Create a quiz application using the Django framework along with SQLite3.

## Project structure

```text
quiz_app/
├── manage.py
├── quiz_app/              # settings & root urls
├── quiz/                  # the quiz app
│   ├── admin.py           # register Question, Choice
│   ├── models.py          # Question, Choice
│   ├── views.py           # quiz & result
│   ├── urls.py
│   └── templates/quiz/
│       ├── quiz.html
│       └── result.html
├── db.sqlite3             # SQLite3 database file
└── static/                # optional CSS, JS, images
```

## Steps

1. **Create an environment and the project:**

   ```bash
   python -m venv week7
   week7\Scripts\activate
   pip install django
   django-admin startproject quiz_app
   cd quiz_app
   python manage.py startapp quiz
   mkdir static
   ```

2. **Edit settings** in [quiz_app/settings.py](open:week07-quiz-app/quiz_app/quiz_app/settings.py): add `'quiz'`, `TEMPLATES`, static folders, time zone `Asia/Kolkata` and the security flags. SQLite3 is Django's default database, so `DATABASES` stays as generated.
3. **Write the models** in [quiz/models.py](open:week07-quiz-app/quiz_app/quiz/models.py). `Choice` links to `Question` with `related_name="choices"`, so a template can loop over `question.choices.all`.
4. **Create the tables:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Register the models** in [quiz/admin.py](open:week07-quiz-app/quiz_app/quiz/admin.py).
6. **Write the views** in [quiz/views.py](open:week07-quiz-app/quiz_app/quiz/views.py). `result_view` reads each answer with `request.POST.get(str(question.id))` and adds 1 for every choice with `is_correct=True`.
7. **Map the URLs** in [quiz/urls.py](open:week07-quiz-app/quiz_app/quiz/urls.py) (app level) and [quiz_app/urls.py](open:week07-quiz-app/quiz_app/quiz_app/urls.py) (project level).
8. **Create the templates** [quiz/templates/quiz/quiz.html](open:week07-quiz-app/quiz_app/quiz/templates/quiz/quiz.html) and [result.html](open:week07-quiz-app/quiz_app/quiz/templates/quiz/result.html). Each radio button's `name` is the question id and its `value` is the choice id.
9. **Add questions.** Run `python manage.py createsuperuser`, open `/admin/`, add Questions, then add Choices and tick *Is correct* on the right one.
10. **Run the project:**

    ```bash
    python manage.py runserver
    ```

    Answer at http://127.0.0.1:8000 ([quiz](open:week07-quiz-app/output/quiz-answered.jpg)) and see the score ([result](open:week07-quiz-app/output/result.jpg)).
