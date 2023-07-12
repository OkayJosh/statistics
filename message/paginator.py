from django.core.paginator import Paginator
from django.db.models import Sum
from django.utils.functional import cached_property

query = """
    SELECT id, customerId, type, COUNT(id) AS num_messages, ROUND(SUM(amount), 3) AS total_amount
    FROM statistics
    WHERE created BETWEEN %s AND %s AND type = %s
    GROUP BY customerId, type
"""


class StatisticPaginator(Paginator):

    @cached_property
    def amount(self):
        """Return the sum of amount in objects, across all pages."""
        try:
            return self.object_list.aggregate(total_amount=Sum('amount')).get('total_amount', 0)
        except AttributeError:
            # 'RawQuerySet' object has no attribute 'aggregate'
            # and cannot chain two raw queryset
            # amount = sum(obj.total_amount for obj in self.object_list)
            return round(sum(obj.total_amount for obj in self.object_list), 3)



