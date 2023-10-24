from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductCreatApiView.as_view()),
    path("<int:pk>/", views.ProductDetailApiView.as_view()),
]
