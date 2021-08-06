from rest_framework_mongoengine import viewsets

from weight.models import Weight
from weight.serializers import WeightSerializer


class WeightView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = WeightSerializer

    def get_queryset(self):
        return Weight.objects.all()
