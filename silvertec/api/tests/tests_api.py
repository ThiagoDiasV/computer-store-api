from rest_framework import status
from .base_apitestcase import BaseAPITestCase
from ..models import Processor


class ProcessorMotherBoardSerializersApiTests(BaseAPITestCase):
    def setUp(self):
        super(ProcessorMotherBoardSerializersApiTests, self).setUp()

    def test_create_processor_on_database(self):
        response_201 = self.client.post(
            self.url_processors, self.correct_processor_to_json, format="json"
        )
        response_400 = self.client.post(
            self.url_processors, self.wrong_processor_to_json, format="json"
        )
        self.assertEqual(response_201.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_400.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_motherboard_on_database(self):
        response_201 = self.client.post(
            self.url_motherboards,
            self.correct_motherboard_to_json,
            format="json",
        )
        response_400 = self.client.post(
            self.url_motherboards, self.wrong_motherboard_to_json
        )
        self.assertEqual(response_201.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_400.status_code, status.HTTP_400_BAD_REQUEST)


class OrdersApiTests(BaseAPITestCase):
    def setUp(self):
        super(OrdersApiTests, self).setUp()

    def test_if_orders_list_is_showed_at_orders_list_url(self):
        response_200 = self.client.get(self.url_orders, format="json")
        self.assertEqual(response_200.status_code, status.HTTP_200_OK)

    def test_if_correct_computer_build_show_http_201(self):
        response_201 = self.client.post(
            self.url_computers, self.correct_computer_to_json, format="json"
        )
        from ipdb import set_trace; set_trace()
        self.assertEqual(response_201.status_code, status.HTTP_201_CREATED)
