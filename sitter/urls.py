from django.urls import path

from . import views


urlpatterns = [
    path("", views.SitterListView .as_view(), name="sitter-list"),
]