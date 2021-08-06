from rest_framework_mongoengine import serializers
from rest_framework_mongoengine.fields import FileField

from origindestiny.models import OriginDestiny
from origindestiny.serializers import OriginDestinySerializer
from weight.models import Weight
from weight.serializers import WeightSerializer
from .business.carrier_business import CarrierBusiness
from .models import Carrier, FreightPrice


class FreightPriceSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = FreightPrice
        depth = 2


class CarrierSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Carrier
        fields = ['id', 'name']


class CarrierFreightPriceSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Carrier
        depth = 2
        fields = ['id', 'freight_prices']

    def create(self, validated_data):

        carrier_id = validated_data['id']
        freight_prices_payload = validated_data['freight_prices']

        business = CarrierBusiness()
        return business.save_carrier_freight_prices(carrier_id, freight_prices_payload)


class FreightPriceCalculatedSerializer(serializers.DocumentSerializer):

    origin_destiny = OriginDestinySerializer(OriginDestiny, many=False)
    weight = WeightSerializer(Weight, many=False)

    class Meta:
        model = FreightPrice
        depth = 2
        fields = ['price', 'expiration', 'origin_destiny', 'weight']


class PriceCalculatedSerializer(serializers.DocumentSerializer):

    freight_prices = FreightPriceCalculatedSerializer(FreightPrice, many=True)

    class Meta:
        model = Carrier
        fields = ['id', 'name', 'freight_prices']


class FileUploadSerializer(serializers.DocumentSerializer):
    file = FileField()
