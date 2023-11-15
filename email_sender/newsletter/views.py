from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from .forms import SubscribedUsersForm

# Create your views here.


def index(request):
    if request.method == "POST":
        form = SubscribedUsersForm(request.POST)

        if form.is_valid():
            form.save()

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            email_from = settings.EMAIL_HOST_USER

            subject = "Newsletter Subscription"
            message = f"Hello {name}, Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email.'"
            recipient_list = [email]

            send_mail(subject, message, None, recipient_list, fail_silently=False)

            return redirect(reverse("thank_you"))
    else:
        form = SubscribedUsersForm()
    return render(request, "newsletter/index.html", context={"form": form})


def thank_you(request):
    return render(request, "newsletter/thank_you.html")
