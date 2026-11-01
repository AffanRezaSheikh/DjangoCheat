# mail/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import MailForm, RegisterForm
from .models import Mail

# Inbox View
@login_required
def inbox_view(request):
    mails = Mail.objects.filter(owner=request.user).order_by('-timestamp')
    return render(request, "mail/inbox.html", {"mails": mails})

# ✉ Compose Mail View
@login_required
def compose_view(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            # Send email via SMTP
            send_mail(subject, body, settings.EMAIL_HOST_USER, [recipient])

            # Save to DB
            Mail.objects.create(
                sender=settings.EMAIL_HOST_USER,
                recipient=recipient,
                subject=subject,
                body=body,
                owner=request.user
            )
            return redirect("inbox")
    else:
        form = MailForm()
    return render(request, "mail/compose.html", {"form": form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("inbox")
    else:
        form = AuthenticationForm()
    return render(request, "mail/login.html", {"form": form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

# Register View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("inbox")
    else:
        form = RegisterForm()
    return render(request, "mail/register.html", {"form": form})
