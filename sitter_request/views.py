from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import SitterRequest
from .serializers import SitterRequestSerializer


# Create your views here.

class SitterRequestListView(APIView):
    """
    A simple view for viewing all sitter_requests
    """

    def get(self, request, format=None):
        # name = request.query_params.get("name") -queryparms
        sitter_requester_id = {"sitter_requester_id": request.data.get("sitter_requester_id")}
        paired_sitter_id = {"paired_sitter_id": request.data.get("paired_sitter_id")}
        try:
            if paired_sitter_id:
                sitter_requests = SitterRequest.objects.filter(paired_sitter_id=paired_sitter_id)
            elif sitter_requester_id:
                sitter_requests = SitterRequest.objects.filter(sitter_requester_id=sitter_requester_id)
            else:    
                raise Http404
            serializer = SitterRequestSerializer(sitter_requests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """
        Create the sitter_request with given data
        """
        data = {"name": request.data.get("name")}
        serializer = SitterRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
