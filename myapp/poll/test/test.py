from unittest.mock import Mock, patch, MagicMock
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework import status
from poll.views import PostViewSet

class Poll_test(APITestCase):

    def setUp(self):
        pass

    #@patch('package.module.ClassName')
    @patch('poll.views.requests', MagicMock(return_value=Mock(status_code=status.HTTP_200_OK)))
    def test_poll_get(self):
        factory = APIRequestFactory()
        view = PostViewSet.as_view()
        request = factory.post('/poll/Tokyo/')
        response = view(request,location = "tokyo")
        self.assertEqual(response.status_code, 200)

