from rest_framework import serializers

from .models import Movies

class Movieserializes(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields='__all__'
