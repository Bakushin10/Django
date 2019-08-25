from django.test import TestCase, Client
from django.urls import reverse
from ocr_api.models import JsonOCRInputModel
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.get_dummy_data_url = reverse("get_dummy_data")

    def test_GET(self):
        response = self.client.get(self.get_dummy_data_url)
        self.assertEquals(response.status_code, 200)
        