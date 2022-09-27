from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from .models import *

# Create your views here.
class GtlFormList(APIView):
    def get(self,request,format=None):
            user=GtlForm.objects.all()
            serializer=GtlFormSerializer(user,many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
            # print(request.data)
            serializer=GtlFormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_201_CREATED)
            return Response(status.HTTP_400_BAD_REQUEST)