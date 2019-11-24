from rest_framework import status
from .base_apitestcase import BaseAPITestCase
from ..models import Computer
from model_bakery import baker
from ..serializers import ComputerSerializer


class ProcessorMotherBoardSerializersApiTests(BaseAPITestCase):
    def setUp(self):
        super().setUp()

    def test_create_processor_on_database(self):
        create_correct_processor_response_201 = self.client.post(
            self.url_processors, self.correct_processor_to_json, format="json"
        )
        create_wrong_processor_response_400 = self.client.post(
            self.url_processors, self.wrong_processor_to_json, format="json"
        )
        self.assertEqual(
            create_correct_processor_response_201.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            create_wrong_processor_response_400.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_create_motherboard_on_database(self):
        create_correct_mb_response_201 = self.client.post(
            self.url_motherboards,
            self.correct_motherboard_to_json,
            format="json",
        )
        create_wrong_mb_response_400 = self.client.post(
            self.url_motherboards, self.wrong_motherboard_to_json
        )
        self.assertEqual(
            create_correct_mb_response_201.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            create_wrong_mb_response_400.status_code,
            status.HTTP_400_BAD_REQUEST,
        )


class OrdersAndComputersBuildApiTests(BaseAPITestCase):
    def setUp(self):
        super().setUp()

    def test_if_orders_list_is_showed_at_orders_list_url(self):
        orders_list_response_200 = self.client.get(
            self.url_orders, format="json"
        )
        self.assertEqual(
            orders_list_response_200.status_code, status.HTTP_200_OK
        )

    def test_if_computers_list_is_showed_at_computers_list_url(self):
        computers_list_response_200 = self.client.get(
            self.url_computers, format="json"
        )
        self.assertEqual(
            computers_list_response_200.status_code, status.HTTP_200_OK
        )

    def test_if_correct_computer_build_show_http_201(self):
        correct_computer_build_response_201 = self.client.post(
            self.url_computers, self.correct_computer_to_json, format="json"
        )
        self.assertEqual(
            correct_computer_build_response_201.status_code,
            status.HTTP_201_CREATED,
        )

    def test_if_wrong_computer_build_show_bad_request(self):
        wrong_computer_build_response_400 = self.client.post(
            self.url_computers, self.wrong_computer_to_json, format="json"
        )
        self.assertEqual(
            wrong_computer_build_response_400.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_if_getting_an_non_existing_instance_shows_http_404(self):
        get_non_existent_motherboard = self.client.get(
            f"{self.url_motherboards}{300*400}/", format="json"
        )
        self.assertEqual(
            get_non_existent_motherboard.status_code, status.HTTP_404_NOT_FOUND
        )

    def test_if_deleting_an_existing_instance_shows_http_204(self):
        delete_first_motherboard = self.client.delete(
            f"{self.url_motherboards}1/", format="json"
        )
        self.assertEqual(
            delete_first_motherboard.status_code, status.HTTP_204_NO_CONTENT
        )

    def test_if_updating_an_instance_shows_http_200(self):
        update_first_graphiccard = self.client.put(
            f"{self.url_graphic_cards}{self.graphic_card_sample['id']}/",
            self.graphic_card_sample,
            format="json",
        )
        self.assertEqual(
            update_first_graphiccard.status_code, status.HTTP_200_OK
        )

    def test_if_no_user_so_no_orders_can_be_made_then_http_400(self):
        fake_computer_instance_id = ComputerSerializer(
            baker.make(Computer)
        ).data["id"]
        post_fake_computer_inside_an_order = self.client.post(
            f"{self.url_orders}",
            {"computer_id": [fake_computer_instance_id]},
            format="json",
        )
        self.assertEqual(
            post_fake_computer_inside_an_order.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
