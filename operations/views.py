from django.shortcuts import render
from rest_framework import generics
from .models import Movies
from .serializers import Movieserializes

class MovieInsert(generics.ListCreateAPIView):
    queryset=Movies.objects.all()
    serializer_class=Movieserializes

class MoviesUpdateAndDelete(generics.ListCreateAPIView):
    queryset=Movies.objects.all()
    serializer_class=Movieserializes
    