from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInstance, Book, Language, Genre, Author
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avail = BookInstance.objects.filter(status__exact="a").count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_avail": num_instances_avail,
    }

    return render(request, "catalog/index.html", context=context)


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = "__all__"


class BookDetail(DetailView):
    model = Book
    fields = "__all__"


@login_required
def my_view(request):
    return render(request, "catalog/my_view.html")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "catalog/signup.html"


class CheckedOutBookByUserView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = "catalog/profile.html"
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).all()
