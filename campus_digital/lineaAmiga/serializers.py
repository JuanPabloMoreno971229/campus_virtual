from rest_framework import serializers
from .models import LineaAmiga

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaAmiga
        fields = '__all__'
