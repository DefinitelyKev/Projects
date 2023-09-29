from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Reviewform


# Create your views here.
def rental_review(request):
    if request.method == "POST":
        form = Reviewform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("cars:thank_you"))
    else:
        form = Reviewform()
    return render(request, "cars/rental_review.html", context={"form": form})


def thank_you(request):
    return render(request, "cars/thank_you.html")
