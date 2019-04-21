from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializers
from .models import Bucketlist
# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines create bahavior of our rest api"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializers
    
    def perform_create(self, serializer):
        
        serializer.save()
