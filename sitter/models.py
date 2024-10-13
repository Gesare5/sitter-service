from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import uuid

from sitterapi.utils import create_id_from_timestamp

# NB:
# find a way to create a new field using existing field, probably on the serializer side
# find out if django- user can be bypassed all together

# THINGS TO TRY
# PERFORM CREATIONS ON THE VIEW ITSELF
# OVERRIDING THE SAVE METHOD INSTEAD OF CREATE
# SCRAP THE INHERITANCE AND USE A 1-1 RELATION, TRY OUT INHERITANCE ON A SMALLER SCALE
# @FIND DOCS ON MODELS & DJANGO USER MODEL

class Sitter(User):
    service_types = (
        (0, "Pet"),
        (1, "House"),
    )


    _id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)
    sitter_id = models.IntegerField(default=create_id_from_timestamp, unique=True, editable=False)

    # first_name = models.CharField(max_length=200, null=True)
    # last_name = models.CharField(max_length=200, null=True)
    # username = models.CharField(max_length=250, unique=True)
    # full_name = models.CharField(max_length=200, null=True)
    # email = models.CharField(max_length=256, unique=True, null=True)
    service_type = models.IntegerField(choices=service_types, default=0) #make this a list/string of comma separated values
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    # user_ptr = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)





# first_name: "Ivy",
# last_name: "June",
# username: "IvyJ",
# email: "ivy@example.com",
# service_type: 0,
#     town: "Juja",
#     country = "Kenya"