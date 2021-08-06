from rest_framework_mongoengine import serializers

from weight.models import Weight


class WeightSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Weight
        fields = ['id', 'min_weight', 'max_weight', 'weight_range']
