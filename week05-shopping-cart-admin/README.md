# Week 5 — Shopping Cart with a Custom Admin Page

**Aim:** Create a shopping cart web application and add a customised admin page for product catalog management (for Experiment 3).

## Project structure

```text
shopping_cart/
├── manage.py
├── shopping_cart/          # project settings
│   ├── settings.py
│   └── urls.py
└── shop/                   # main app
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
        ├── base.html
        ├── registration.html
        ├── login.html
        ├── catalog.html
        └── cart.html
```

## Steps

1. **Set up the project:**

   ```bash
   python -m venv week5
   week5\Scripts\activate
   pip install django
   django-admin startproject shopping_cart
   cd shopping_cart
   python manage.py startapp shop
   ```

2. **Edit settings.** In [shopping_cart/settings.py](open:week05-shopping-cart-admin/shopping_cart/shopping_cart/settings.py) add `'shop'` to `INSTALLED_APPS` and set `LOGIN_URL`, `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL`.
3. **Write the views** in [shop/views.py](open:week05-shopping-cart-admin/shopping_cart/shop/views.py): `register`, `catalog`, `add_to_cart`, `cart` and `update_cart`. All except `register` use `@login_required`.
4. **Write the models** in [shop/models.py](open:week05-shopping-cart-admin/shopping_cart/shop/models.py): `Product` (name, price, description) and `CartItem` (user, product, quantity) with a `subtotal()` method.
5. **Write the forms** in [shop/forms.py](open:week05-shopping-cart-admin/shopping_cart/shop/forms.py): `RegistrationForm` (extends `UserCreationForm` with email) and `CartItemForm` (quantity only).
6. **Customise the admin** in [shop/admin.py](open:week05-shopping-cart-admin/shopping_cart/shop/admin.py). `list_display` picks the columns, `search_fields` adds the search box — this is the custom product catalog page.
7. **Map the URLs** in [shop/urls.py](open:week05-shopping-cart-admin/shopping_cart/shop/urls.py) (login and logout use Django's built-in `LoginView` and `LogoutView`) and include them from [shopping_cart/urls.py](open:week05-shopping-cart-admin/shopping_cart/shopping_cart/urls.py).
8. **Create the templates** in `shop/templates/`: [base.html](open:week05-shopping-cart-admin/shopping_cart/shop/templates/base.html), [registration.html](open:week05-shopping-cart-admin/shopping_cart/shop/templates/registration.html), [login.html](open:week05-shopping-cart-admin/shopping_cart/shop/templates/login.html), [catalog.html](open:week05-shopping-cart-admin/shopping_cart/shop/templates/catalog.html) and [cart.html](open:week05-shopping-cart-admin/shopping_cart/shop/templates/cart.html). Each page `{% extends 'base.html' %}`.
9. **Create the database and an admin user:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

10. **Add products** at http://127.0.0.1:8000/admin/ → *Products* → *Add product* ([screenshot](open:week05-shopping-cart-admin/output/admin-add-product.jpg)).
11. **Use the shop.** There is no page at `/` ([404 screenshot](open:week05-shopping-cart-admin/output/404-root.jpg)), so start at http://127.0.0.1:8000/register/ or `/catalog/`. Add items, then change quantities in the cart and press **Update**.
