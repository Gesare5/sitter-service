from django.urls import path

from . import views


urlpatterns = [
    path("", views.SitterListView .as_view(), name="sitter-list"),
    path("sitters-in-area/", views.SitterChoiceListView.as_view(), name="sitter-choice-list"),
]