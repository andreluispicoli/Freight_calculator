from datetime import datetime

from mongoengine import fields, Document, signals, EmbeddedDocument, EmbeddedDocumentField


class FreightPrice(EmbeddedDocument):
    origin_destiny = fields.ReferenceField('OriginDestiny', required=True)
    weight = fields.ReferenceField('Weight', required=True)
    price = fields.DecimalField(required=True)
    expiration = fields.DateTimeField(required=True)
    created_at = fields.DateTimeField(default=datetime.now(), assign=True)
    updated_at = fields.DateTimeField(default=datetime.now(), assign=True)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now()


class Carrier(Document):
    name = fields.StringField(required=True)
    freight_prices = fields.ListField(EmbeddedDocumentField(FreightPrice))
    created_at = fields.DateTimeField(default=datetime.now(), assign=True)
    updated_at = fields.DateTimeField(default=datetime.now(), assign=True)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now()

    @staticmethod
    def get_by_id(carrier_id):
        return Carrier.objects.get(id=carrier_id)

    def save_instance(self, update_fields=[]):
        self.save(update_fields=update_fields) if update_fields else self.save()


signals.pre_save.connect(Carrier.pre_save, sender=Carrier)
signals.pre_save.connect(FreightPrice.pre_save, sender=FreightPrice)

