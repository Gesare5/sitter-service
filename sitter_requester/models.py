from django.db import models

import uuid



class SitterRequester(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)
    sitter_requester_id = models.IntegerField()
    full_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    service_type = models.CharField(max_length=100, null=True)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
