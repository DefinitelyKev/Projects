from django.shortcuts import render
from .models import Project


# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    context = {"projects": projects}

    return render(request, "index.html", context)


def full_view(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}

    return render(request, "full_view.html", context)
