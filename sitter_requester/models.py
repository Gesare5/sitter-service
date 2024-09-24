from django.db import models
from django.utils import timezone

import uuid



class SitterRequester(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)
    sitter_requester_id = models.IntegerField(null=False)
    full_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    service_type = models.CharField(max_length=100, null=True)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
