from django.db import models
from django.utils import timezone

import uuid

from sitter_requester.models import SitterRequester



class SitterRequest(models.Model):
    status_types = (
    (0, "Created"),
    (1, "Matched"),
    (2, "Completed"),
    (3, "Canceled"),
    )
    service_types = (
        (0, "Pet"),
        (1, "House"),
    )
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    service_type = models.IntegerField(choices=service_types, default=0)
    service_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=status_types, default=0)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sitter_requester_id = models.ForeignKey(SitterRequester, null=True, on_delete=models.SET_NULL)
    attempt_sitter_pair_id = models.CharField(max_length=200)    #should be null
    paired_sitter_id = models.CharField(max_length=200)           #should be null
    number_of_pets = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
  