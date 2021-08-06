from mongoengine import ValidationError
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets, generics
from rest_framework_mongoengine.viewsets import GenericViewSet

from api.exceptions import BadRequestException
from carrier.business.price_business import PriceBusiness
from carrier.models import Carrier
from carrier.serializers import CarrierSerializer, CarrierFreightPriceSerializer, PriceCalculatedSerializer, \
    FileUploadSerializer


class CarrierView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = CarrierSerializer

    def get_queryset(self):
        return Carrier.objects.all()


class FreightPriceView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = CarrierFreightPriceSerializer

    def get_queryset(self):
        return Carrier.objects.all()

    def create(self, request, *args, **kwargs):

        if not request.data['_id']:
            return Response({"Message": "Request has no carrier id!"}, status=400)

        serializer = CarrierFreightPriceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValidationError):
            serializer.save(id=request.data['_id'])
            return Response({"Message": "Prices successfully registered!"}, status=201)


class PriceCalculatedView(mixins.ListModelMixin,
                          GenericViewSet
                          ):
    lookup_field = 'id'
    serializer_class = PriceCalculatedSerializer
    queryset = Carrier.objects.all()

    def list(self, request, *args, **kwargs):

        origin = self.request.GET.get('origin')
        destiny = self.request.GET.get('destiny')
        product_weight = self.request.GET.get('product_weight')

        if None in (origin, destiny):
            raise BadRequestException("'origin' or 'destiny' was not given")

        if product_weight is None:
            raise BadRequestException("'product_weight' was not given")

        lowest_freight_price = PriceBusiness().get_lowest_freight_price(origin, destiny, product_weight)

        serializer = self.get_serializer(lowest_freight_price)

        return Response(data=serializer.data, status=200)


class CarrierPricesImportView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)




