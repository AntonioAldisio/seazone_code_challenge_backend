import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.conf import settings
from django.core.management import call_command


class ApiTestCase(TestCase):

    def setUp(self):
        self._migrate_test_database()
        self.client = APIClient()
        self.url = '/api/anuncios/'

    def _migrate_test_database(self):
        settings.DATABASES['default'] = settings.DATABASES['test']
        call_command('makemigrations')
        call_command('migrate')
        call_command('loaddata', 'test_seeder.json')

    def test_get_endpoint(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(len(data) > 0)

    def test_get_with_filter(self):
        params = {
            'plataforma': 'AirBnb'
        }
        response = self.client.get(self.url, params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(len(data) > 0)

    def test_post_endpoint(self):
        data = {
            "codigo_imovel": 1,
            "plataforma": "Booking",
            "taxa_plataforma": "15.00",
            "imovel": 1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.parametrize("id", [1, 2])
    def test_put_endpoint(self):
        data = {
            "codigo_imovel": 1,
            "plataforma": "Booking",
            "taxa_plataforma": "25.00",
            "imovel": 1
        }
        response = self.client.put(self.url + f'{id}/', data)
        if response.status_code == 200:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            updated_data = response.json()
            self.assertEqual(updated_data['plataforma'], "Booking")
            self.assertEqual(updated_data['taxa_plataforma'], "25.00")
        else:
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
