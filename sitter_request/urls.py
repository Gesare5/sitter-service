from django.urls import path

from . import views


urlpatterns = [
    path("", views.SitterRequestListView .as_view(), name="sitter-request-list"),
    path("<int:pk>/", views.SitterRequestDetailView.as_view(), name="sitter-request-detail"),
    path("<int:pk>/pair", views.SitterRequestPairView.as_view(), name="sitter-request-pair"),
    path("<int:pk>/cancel", views.SitterRequestCancelView.as_view(), name="sitter-request-cancel"),
]