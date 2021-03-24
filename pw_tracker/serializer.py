from rest_framework import serializers
from .models import Tracker

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'website', 'updated_at')
        model = Tracker