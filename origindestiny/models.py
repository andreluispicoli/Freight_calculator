from datetime import datetime

from mongoengine import Document, fields, signals


class OriginDestiny(Document):
    origin = fields.StringField(required=True)
    destiny = fields.StringField(required=True)
    created_at = fields.DateTimeField(default=datetime.now(), assign=True)
    updated_at = fields.DateTimeField(default=datetime.now(), assign=True)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now()

    @staticmethod
    def get_by_id(origin_destiny_id):
        return OriginDestiny.objects.get(id=origin_destiny_id)

    @staticmethod
    def get_origin_destiny_by_name(origin, destiny):
        return OriginDestiny.objects.get(origin=origin, destiny=destiny)


signals.pre_save.connect(OriginDestiny.pre_save, sender=OriginDestiny)
