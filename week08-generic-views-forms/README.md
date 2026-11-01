# Week 8 — Generic Views and Forms

**Aim:** Create a Django application using generic views and forms.

**Generic views** are part of Django's class-based views (CBVs). They handle common patterns — listing objects, showing details, creating, updating and deleting records.

| View type | Purpose | Class name |
|---|---|---|
| List View | Display a list of objects | `ListView` |
| Detail View | Show details of a single object | `DetailView` |
| Create View | Handle the form for creating an object | `CreateView` |
| Update View | Handle the form for updating an object | `UpdateView` |
| Delete View | Confirm and delete an object | `DeleteView` |

**Generic forms** are Django's built-in form classes that simplify form creation and handling.

| Form type | Description |
|---|---|
| `Form` | Basic form with manually defined fields |
| `ModelForm` | Auto-generates fields from a Django model |
| `FormView` | Generic view for displaying and processing forms |

## Steps

1. **Create the project and app:**

   ```bash
   python -m venv week8
   week8\Scripts\activate
   pip install django
   django-admin startproject library
   cd library
   python manage.py startapp bookmanager
   ```

   Add `'bookmanager'` to `INSTALLED_APPS` in [library/settings.py](open:week08-generic-views-forms/library/library/settings.py).
2. **Write the model** in [bookmanager/models.py](open:week08-generic-views-forms/library/bookmanager/models.py): `Book` with title, author, published_date and genre.
3. **Create the tables:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Write the form** in [bookmanager/forms.py](open:week08-generic-views-forms/library/bookmanager/forms.py): a `ModelForm` for `Book`.
5. **Write the generic views** in [bookmanager/views.py](open:week08-generic-views-forms/library/bookmanager/views.py). Each class only sets `model`, `template_name` and, for create/update/delete, `success_url = reverse_lazy('book_list')`.
6. **Map the URLs** in [bookmanager/urls.py](open:week08-generic-views-forms/library/bookmanager/urls.py). Class-based views are added with `.as_view()`; `<int:pk>` passes the book's id.
7. **Include them** in the main [library/urls.py](open:week08-generic-views-forms/library/library/urls.py).
8. **Create the templates** in `bookmanager/templates/`:
   1. [base.html](open:week08-generic-views-forms/library/bookmanager/templates/base.html)
   2. [book_list.html](open:week08-generic-views-forms/library/bookmanager/templates/book_list.html) — loops over `object_list`
   3. [book_detail.html](open:week08-generic-views-forms/library/bookmanager/templates/book_detail.html) — shows `object`
   4. [book_form.html](open:week08-generic-views-forms/library/bookmanager/templates/book_form.html) — used for both Add and Edit
   5. [book_confirm_delete.html](open:week08-generic-views-forms/library/bookmanager/templates/book_confirm_delete.html)
9. **Run the application:**

   ```bash
   python manage.py runserver
   ```

   Add a book (type the date as `2008-11-18`), open it, edit it and delete it. Compare with the [output screenshots](open:week08-generic-views-forms/output/book-list.jpg).
