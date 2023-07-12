import uuid as uuid
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Statistic(TimeStampedModel):
    # This default values are include for ease of filtering
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                          help_text=_("The Primary key"))
    customerId = models.IntegerField(default=000,
                                     help_text=_("The customerId is the customer unique identifier"))
    type = models.CharField(max_length=255, default='AAA',
                            help_text=_("The type of message received"))
    amount = models.DecimalField(max_digits=10, decimal_places=3, default=0.000,
                                 help_text=_("Amount billed to the customer, as a string with 3 decimals precision"))
    uuid = models.UUIDField(default=uuid.uuid4,
                            help_text=_("The message unique identifier"))

    class Meta:
        db_table = 'statistics'

    def __str__(self):
        return str(self.uuid)

