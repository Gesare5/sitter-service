from django.db import models

# Create your models here.

class SitterRequester(models.Model):
    sitter_requester_id = models.CharField(max_length=200, null=True) #set as pk and use uuid
    full_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    service_type = models.CharField(max_length=100, null=True)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


# sitter_requester_id = models.CharField(primary_key=True, null=False) #set as pk and use uuid
#     full_name = models.CharField(max_length=200, null=False)
#     email = models.CharField(max_length=200, null=False)
#     service_type = models.CharField(null=False)
#     town = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)