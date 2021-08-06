from datetime import datetime

from mongoengine import fields, signals, Document


class Weight(Document):
    min_weight = fields.DecimalField(required=True)
    max_weight = fields.DecimalField(required=True)
    weight_range = fields.StringField(required=True)
    created_at = fields.DateTimeField(default=datetime.now(), assign=True)
    updated_at = fields.DateTimeField(default=datetime.now(), assign=True)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now()

    @staticmethod
    def get_by_id(weight_id):
        return Weight.objects.get(id=weight_id)

    @staticmethod
    def get_weight_range(weight):
        return Weight.objects.get(
            min_weight__lte=weight,
            max_weight__gte=weight
        )


signals.pre_save.connect(Weight.pre_save, sender=Weight)
