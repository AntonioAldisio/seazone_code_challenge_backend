from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.conf import settings
from django.core.management import call_command
from api.views import ReservaViewSet


class ApiTestCase(TestCase):

    def setUp(self):
        self._migrate_test_database()
        self.client = APIClient()
        self.url = '/api/reserva/'
        self.viewset = ReservaViewSet()

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
            'codigo_reserva': 'PQR678'
        }
        response = self.client.get(self.url, params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(len(data) > 0)

    def test_create_reservation(self):
        request_data = {
            'id_anuncio': 1,
            'data_checkin': '2031-08-01',
            'data_checkout': '2031-09-05',
            'preco_total': '1000.00',
            'comentario': 'Reserva de teste',
            'numero_hospedes': 2,
            'anuncio': 1,
        }

        response = self.client.post(self.url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.parametrize("id", [1, 2])
    def test_delete_endpoint(self):
        response = self.client.delete(self.url + f'{id}/')
        if response.status_code == 200:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            response = self.client.get(self.url + f'{id}/')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        else:
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
