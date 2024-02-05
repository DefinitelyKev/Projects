from django.urls import path
from .views import full_view, project_list, hello


urlpatterns = [
    path("", project_list, name="index"),
    path("<int:pk>/", full_view, name="full_view"),
    path("hello/", hello, name="hello"),
]
