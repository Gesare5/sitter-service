from django.db import models

from sitter_requester.models import SitterRequester
# Create your models here.

class SitterRequest(models.Model):
    request_id = models.CharField(max_length=200, null=True) #set as pk and use uuid
    service_type = models.CharField(max_length=100, null=True)
    service_date = models.DateTimeField(auto_now_add=True)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sitter_requester_id = models.ForeignKey(SitterRequester, null=True, on_delete=models.SET_NULL)
    attempt_sitter_pair_id = models.CharField(max_length=200)
    paired_sitter_id = models.CharField(max_length=200)
    number_of_pets = models.IntegerField(default=1)


    #     request_id = models.CharField(primary_key=True, null=False) #set as pk and use uuid
    # service_type = models.CharField(null=False)
    # service_date = models.DateTimeField(auto_now_add=True)
    # town = models.CharField(max_length=100)
    # country = models.CharField(max_length=100)
    # sitter_requester_id = models.ForeignKey(SitterRequester.sitter_requester_id, null=True, on_delete=models.SET_NULL)
    # attempt_sitter_pair_id = models.CharField()
    # paired_sitter_id = models.CharField()
    # number_of_pets = models.IntegerField(default=1)