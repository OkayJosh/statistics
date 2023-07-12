from django_filters import rest_framework as filters


from holder.models import Statistic


class StatisticFilter(filters.FilterSet):
    customer = filters.NumberFilter(field_name='customerId', lookup_expr='iexact')

    amount__gt = filters.NumberFilter(field_name='amount', lookup_expr='gt')
    amount__lt = filters.NumberFilter(field_name='amount', lookup_expr='lt')

    from_date = filters.DateTimeFilter(field_name='created', lookup_expr='gt')
    to_date = filters.DateTimeFilter(field_name='created', lookup_expr='lt')

    created__year = filters.NumberFilter(field_name='created', lookup_expr='year')
    created__year__gt = filters.NumberFilter(field_name='created', lookup_expr='year__gt')
    created__year__lt = filters.NumberFilter(field_name='created', lookup_expr='year__lt')

    class Meta:
        model = Statistic
        fields = ['customerId', 'type', 'created', 'amount', 'uuid']
