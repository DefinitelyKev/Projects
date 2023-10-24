from django.urls import path
from .views import full_view, project_list


urlpatterns = [
    path("", project_list, name="index"),
    path("<int:pk>/", full_view, name="full_view"),
]
