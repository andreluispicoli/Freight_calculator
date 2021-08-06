from carrier.models import Carrier
from origindestiny.models import OriginDestiny
from weight.models import Weight


class PriceBusiness:

    def get_lowest_freight_price(self, origin, destiny, product_weight):
        origin_destiny = OriginDestiny.get_origin_destiny_by_name(origin, destiny)
        weight_range = Weight.get_weight_range(product_weight)
        return self._get_lowest_price_of_freight_by_origin_destiny_and_weight(origin_destiny, weight_range)

    @staticmethod
    def _get_lowest_price_of_freight_by_origin_destiny_and_weight(origin_destiny_id, weight_range):
        return Carrier.objects(
            freight_prices__origin_destiny=origin_destiny_id,
            freight_prices__weight=weight_range
        ).order_by('freight_prices__price').first()
