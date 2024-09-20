from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import SitterRequester
from .serializers import SitterRequesterSerializer

class SitterRequesterListView(APIView):
    """
    A simple view for viewing all sitter_requests
    """

    def get(self, request, format=None):
        try:
            sitter_requester = SitterRequester.objects.all()
            serializer = SitterRequesterSerializer(sitter_requester, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
