from django.urls import path
from pages.views import home, UploadView

urlpatterns = [
    path("", home, name="home"),
    path("upload/", UploadView.as_view(), name="upload"),
]
