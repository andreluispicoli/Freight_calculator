from rest_framework_mongoengine import serializers

from .models import OriginDestiny


class OriginDestinySerializer(serializers.DocumentSerializer):
    class Meta:
        model = OriginDestiny
        fields = ['id', 'origin', 'destiny']
