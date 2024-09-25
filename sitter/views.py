from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Sitter
from .serializers import SitterSerializer

class SitterListView(APIView):
    """
    A simple view for viewing all sitter_requests
    """

    def get(self, request, format=None):
        try:
            sitter = Sitter.objects.all()
            
            serializer = SitterSerializer(sitter, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SitterChoiceListView(APIView):
    """
    A simple view for viewing all sitter_requests
    """

    def get(self, request, format=None):
        try:
            town = request.data.get("town")
            country = request.data.get("country")
            sitters = Sitter.objects.filter(town=town, country=country)  # check and vs or filter operations
            
            serializer = SitterSerializer(sitters, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
