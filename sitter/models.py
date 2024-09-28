from django.db import models
from django.utils import timezone

import uuid

from sitterapi.utils import create_id_from_timestamp


class Sitter(models.Model):
    service_types = (
        (0, "Pet"),
        (1, "House"),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)
    sitter_id = models.IntegerField(default=create_id_from_timestamp, unique=True, editable=False)
    full_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=256, unique=True, null=True)
    service_type = models.IntegerField(choices=service_types, default=0)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
