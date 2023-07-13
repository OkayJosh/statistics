from django.test import TestCase
from rest_framework.reverse import reverse

from decimal import Decimal

from holder.models import Statistic


class StatisticViewSetTestCase(TestCase):

    @staticmethod
    def local_data():
        return [
            {"customerId": 1,
             "type": "AAB",
             "amount": "100.876",
             "uuid": "a596b362-08be-419f-8070-9c3055566e7c", },
            {"customerId": 1,
             "type": "AAC",
             "amount": "200.876",
             "uuid": "a596b362-08be-419f-8070-9c3055566e7c", },
            {"customerId": 2,
             "type": "AAB",
             "amount": "100.876",
             "uuid": "a596b362-08be-419f-8070-9c3055566e9c", }
        ]

    @classmethod
    def setUpTestData(cls):
        # this should not cause performance issue for now, data is limited to 3
        for data in cls.local_data():
            Statistic.objects.create(**data)

    def test_get_message_endpoint(self):
        get_message_endpoint = reverse('message-list')
        get_message_response = self.client.get(get_message_endpoint)
        self.assertEqual(get_message_response.status_code, 200)
        self.assertEqual(get_message_response.data['total_message'], 3)
        self.assertEqual(get_message_response.data['total_amount'], Decimal("402.628"))

    def test_get_message_endpoint_with_filters(self):
        get_message_endpoint = reverse('message-list')
        get_message_response = self.client.get(f"{get_message_endpoint}?type=AAB")
        self.assertEqual(get_message_response.status_code, 200)
        self.assertEqual(get_message_response.data['total_message'], 2)
        self.assertEqual(get_message_response.data['total_amount'], Decimal("201.752"))

    def test_create_message(self):
        get_message_endpoint = reverse('message-list')
        get_message_response = self.client.post(path=get_message_endpoint, data=self.local_data()[2])
        self.assertEqual(get_message_response.status_code, 201)

    def test_statistics_endpoint(self):
        get_statistics_endpoint = reverse('message-statistics')
        get_message_response = self.client.get(get_statistics_endpoint)
        self.assertEqual(get_message_response.status_code, 200)
        self.assertEqual(get_message_response.data['total_message'], 3)

    def test_statistics_endpoint_with_type_filter(self):
        get_statistics_endpoint = reverse('message-statistics')
        get_message_response = self.client.get(f"{get_statistics_endpoint}?type=AAB")
        self.assertEqual(get_message_response.status_code, 200)
        self.assertEqual(get_message_response.data['total_message'], 2)

    def test_statistics_endpoint_with_type_date(self):
        get_statistics_endpoint = reverse('message-statistics')
        get_message_response = self.client.get(f"{get_statistics_endpoint}?type=AAB&from_date=2023-07-12")
        self.assertEqual(get_message_response.status_code, 200)
        self.assertEqual(get_message_response.data['total_message'], 2)
