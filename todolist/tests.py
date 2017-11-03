from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            'name': 'Выполнить 9 лабораторную работу',
            'description': 'Прочитать руководство по django rest framework',
            'priority': 'h'
        }
        self.response = self.client.post(reverse('create'),
                                         self.task_data,
                                         format='json')

    def test_api_can_create_a_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
