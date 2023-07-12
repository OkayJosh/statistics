from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from message.paginator import StatisticPaginator


class StatisticPagination(PageNumberPagination):
    """
        this change count to total_message
        and also add total_amount as a sum of all amount in the data
    """

    django_paginator_class = StatisticPaginator

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total_message', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
            ('total_amount', self.page.paginator.amount),
            # ('statistics', self.page.paginator.statistics)
        ]))
