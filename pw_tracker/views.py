from django.shortcuts import render
from rest_framework import generics
from .serializer import PostSerializer
from .models import Tracker
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from pw_tracker.permissions import IsOwnerOrReadOnly

class TrackerList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tracker.objects.all()
    serializer_class = PostSerializer

class TrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Tracker.objects.all()
    serializer_class = PostSerializer

