from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from holder.filters import StatisticFilter
from holder.models import Statistic
from holder.serializers import StatisticSerializers, StatisticInfoSerializers
from message.pagination import StatisticPagination
from message.paginator import query


class StatisticViewSet(ModelViewSet):
    serializer_class = StatisticSerializers
    info_serializer_class = StatisticInfoSerializers
    filter_class = StatisticFilter
    pagination_class = StatisticPagination

    def get_queryset(self):
        queryset = Statistic.objects.all()
        filter_params = self.request.query_params.dict()

        # Apply filtering using the StatisticFilter
        filter_set = self.filter_class(data=filter_params, queryset=queryset, request=self.request)
        if filter_set.is_valid():
            queryset = filter_set.qs.order_by('id')

        return queryset

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        filter_params = self.request.query_params.dict()
        args = []

        from_date = filter_params.get('from_date', '0000-00-00').split('T', 1)[0]
        args.append(from_date)

        to_date = filter_params.get('to_date', '9999-12-31').split('T', 1)[0]
        args.append(to_date)

        message_type = filter_params.get('type', None)

        type_filter = ""

        if message_type is not None:
            type_filter = "AND type = %s"
            args.append(message_type)

        final_query = query.format(type_filter=type_filter)

        queryset = Statistic.objects.raw(final_query, args)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.info_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.info_serializer_class(queryset, many=True)
        return Response(serializer.data)
