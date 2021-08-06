from carrier.models import Carrier, FreightPrice
from origindestiny.models import OriginDestiny
from weight.models import Weight


class CarrierBusiness:

    @staticmethod
    def save_carrier_freight_prices(carrier_id, freight_prices_payload):
        carrier = Carrier.get_by_id(carrier_id)
        for freight_price in freight_prices_payload:
            origin_destiny = OriginDestiny.get_by_id(freight_price['origin_destiny'].id)
            weight = Weight.get_by_id(freight_price['weight'].id)
            carrier.freight_prices.append(FreightPrice(
                origin_destiny=origin_destiny,
                weight=weight,
                price=freight_price['price'],
                expiration=freight_price['expiration']
            ))
        carrier.save_instance(update_fields=['freight_prices'])
        return carrier
