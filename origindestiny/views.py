from rest_framework_mongoengine import viewsets

from origindestiny.serializers import OriginDestinySerializer
from origindestiny.models import OriginDestiny


class OriginDestinyView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = OriginDestinySerializer

    def get_queryset(self):
        return OriginDestiny.objects.all()
