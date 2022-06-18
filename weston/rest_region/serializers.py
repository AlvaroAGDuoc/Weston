from rest_framework import serializers
from app.models import Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['nombre']
