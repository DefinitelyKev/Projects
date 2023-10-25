from django.urls import path
from .views import signup, thankYouView

urlpatterns = [
    path("", signup, name="signup"),
    path("thank_you/", thankYouView, name="thank_you"),
]
