from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
from .forms import EmailForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = EmailForm(request.POST)

        if form.is_valid():
            cleaned_form = form.cleaned_data

            email_from = settings.EMAIL_HOST_USER
            # password = settings.EMAIL_HOST_PASSWORD

            # user = User.objects.create_user(
            #     username="Test User", password=password, email=email_from
            # )

            # login(request, user)

            # name = cleaned_form["name"]
            email = cleaned_form["email"]
            subject = cleaned_form["subject"]
            description = cleaned_form["description"]
            recipient_list = [email, "kevinnk259@gmail.com"]
            send_mail(subject, description, email_from, recipient_list)

            form.save()
            return redirect(reverse("thank_you"))
    else:
        form = EmailForm()
    return render(request, "newsletter/home.html", context={"form": form})


def thankYouView(request):
    return render(request, "newsletter/thank_you.html")
