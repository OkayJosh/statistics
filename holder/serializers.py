from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from holder.models import Statistic


class StatisticSerializers(ModelSerializer):
    class Meta:
        model = Statistic
        fields = [
            'customerId', 'type', 'amount', 'uuid', 'created',
        ]


class StatisticInfoSerializers(serializers.Serializer):
    # customerId, type, COUNT(id) AS num_messages, SUM(amount) AS total_amount
    customerId = serializers.IntegerField(read_only=True)
    type = serializers.CharField(read_only=True)
    num_messages = serializers.IntegerField(read_only=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=3, read_only=True)
