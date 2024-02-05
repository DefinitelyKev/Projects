from django.shortcuts import render
from . import models


# Create your views here.
def list_patients(request):
    all_patients = models.Patient.objects.all()
    return render(request, "office/list.html", context={"patients": all_patients})
