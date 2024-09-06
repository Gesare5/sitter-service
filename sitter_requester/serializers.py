from rest_framework import serializers

from .models import SitterRequester


class  SitterRequesterSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitterRequester
        fields = "__all__"