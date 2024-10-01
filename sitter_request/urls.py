from django.urls import path

from . import views


urlpatterns = [
    path("", views.SitterRequestListView .as_view(), name="sitter-request-list"),
    path("<pk>/", views.SitterRequestDetailView.as_view(), name="sitter-request-detail"),
    path("<pk>/attempt_pair", views.SitterRequestAttemptPairView.as_view(), name="sitter-request-attempt-pair"),
    path("<pk>/pair", views.SitterRequestPairView.as_view(), name="sitter-request-pair"),
    path("<pk>/cancel", views.SitterRequestCancelView.as_view(), name="sitter-request-cancel"),
]


    # path("<pk>/pair", views.SitterRequestPairView.as_view(), name="sitter-request-pair"),
