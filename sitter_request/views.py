from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime

from .models import SitterRequest
from .serializers import SitterRequestSerializer


# Create your views here.

class SitterRequestListView(APIView):
    """
    A simple view for viewing all sitter_requests
    """

    def get(self, request, format=None):
        # request_status = request.query_params.get("status") #from queryparms
        # sitter_requester_id = request.data.get("sitter_requester_id") #from body
        # paired_sitter_id = request.data.get("paired_sitter_id")   
        # try:    
        #     if paired_sitter_id:
        #         sitter_requests = SitterRequest.objects.filter(paired_sitter_id=paired_sitter_id, status=request_status)
        #     elif sitter_requester_id:
        #         sitter_requests = SitterRequest.objects.filter(sitter_requester_id=sitter_requester_id, status=request_status)
        #     else:    
        sitter_requests = SitterRequest.objects.all() #filter by user 

        serializer = SitterRequestSerializer(sitter_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # except:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """
        Create the sitter_request with given data
        """
        data = {"service_date": request.data.get("service_date"),
                "service_type": request.data.get("service_type"),
                "country": request.data.get("country"),
                "town": request.data.get("town"),
                "name": request.data.get("name")}
        
        serializer = SitterRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SitterRequestDetailView(APIView):
    """
    Update Sitter Request details
    Retrieve Sitter Request,
    Change detail,
    Save changes to db
    """

    def get_object(self, pk):
        try:
            return SitterRequest.objects.get(pk=pk)
        except SitterRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sitter_request = self.get_object(pk)
        serializer = SitterRequestSerializer(sitter_request)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        sitter_request = self.get_object(pk)
        if not sitter_request:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = SitterRequestSerializer(sitter_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        sitter_request = self.get_object(pk)
        sitter_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SitterRequestAttemptPairView(APIView):
    """
    Get Request Object 
    Set attempt_sitter_pair_id
    save
    """                                            

    def get_object(self, pk):
        try:
            return SitterRequest.objects.get(pk=pk)
        except SitterRequest.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        sitter_request = self.get_object(pk)
        if not sitter_request:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = SitterRequestSerializer(sitter_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SitterRequestPairView(APIView):
    """
    Get Request Object 
    Set status and pair ids, updated_at timestamps
    save
    """                                              # RETHINK THIS IMPLEMENTATION

    def get_object(self, pk):
        try:
            return SitterRequest.objects.get(pk=pk)
        except SitterRequest.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        sitter_request = self.get_object(pk)
        if not sitter_request:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = SitterRequestSerializer(sitter_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
class SitterRequestCancelView(APIView):
    """
    Get Request Object 
    Set status, updated_at timestamps
    save
    """                                             

    def get_object(self, pk):
        try:
            return SitterRequest.objects.get(pk=pk)
        except SitterRequest.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        sitter_request = self.get_object(pk)
        if not sitter_request:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = SitterRequestSerializer(sitter_request, data=request.data)
        # print out this serializer data
        print('SitterRequestCancelView', serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

         