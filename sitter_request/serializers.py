from rest_framework import serializers

from .models import SitterRequest


class  SitterRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitterRequest
        fields = "__all__"