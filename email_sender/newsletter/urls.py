from django.urls import path
from .views import index, thank_you

urlpatterns = [
    path("", index, name="index"),
    path("thank_you/", thank_you, name="thank_you"),
]
