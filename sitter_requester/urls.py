from django.urls import path

from . import views


urlpatterns = [
    path("", views.SitterRequesterListView .as_view(), name="sitter-requester-list"),
]