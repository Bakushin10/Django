from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ocr_api.views import post_dummy_data, post_ocr_results, get_ocr_results, get_ocred_image, get_dummy_data, get_ocr_results_by_id

class TestUrls(SimpleTestCase):

    def test_get_dummy_data_url_is_resolved(self):
        url = reverse("get_dummy_data")
        self.assertEquals(resolve(url).func, get_dummy_data)

    def test_post_dummy_data_url_is_resolved(self):
        url = reverse("post_dummy_data")
        self.assertEquals(resolve(url).func, post_dummy_data)

    def test_post_ocr_results_data_url_is_resolved(self):
        url = reverse("post_ocr_results")
        self.assertEquals(resolve(url).func, post_ocr_results)
    
    def test_get_ocr_results_url_is_resolved(self):
        url = reverse("get_ocr_results")
        self.assertEquals(resolve(url).func, get_ocr_results)

    def test_get_ocr_results_by_id_url_is_resolved(self):
        url = reverse("get_ocr_results_by_id", args=[1090])
        self.assertEquals(resolve(url).func, get_ocr_results_by_id)

    def test_get_ocred_image_url_is_resolved(self):
        url = reverse("get_ocred_image")
        self.assertEquals(resolve(url).func, get_ocred_image)
    
