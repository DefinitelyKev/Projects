from django.shortcuts import render
from django.views.generic.base import View
from csv import DictReader
from io import TextIOWrapper

from .forms import UploadForm, ProductForm


# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})


class UploadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/upload.html", {"form": UploadForm()})

    def post(self, request, *args, **kwargs):
        products_file = request.FILES["products_file"]
