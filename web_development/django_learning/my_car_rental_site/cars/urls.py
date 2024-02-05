from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("rental_review/", views.rental_review, name="rental_review"),
    path("thank_you/", views.thank_you, name="thank_you"),
]
