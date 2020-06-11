from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from onix import settings
# from locations.models import User
import random
import string


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_create_account(self):
        url = reverse('locations_api:register')
        data = {
            'username': ''.join(random.choice(string.ascii_lowercase) for i in range(12)),
            'password': ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_country(self):
        url = reverse('locations_api:countries')
        data = {
            'name': ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
            'description': ''.join(random.choice(string.ascii_lowercase) for i in range(70)),
            'population': random.randint(10000, 9999999),
            'flag_url': "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/1024px-Flag_of_Japan.svg.png"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_city(self):
        url = reverse('locations_api:register')
        data = {
            'name': ''.join(random.choice(string.ascii_lowercase) for i in range(12)),
            'country': random.randint(10, 40),
            'longitude': random.randint(10000, 9999999),
            'latitude': random.randint(10000, 9999999),
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_country_get(self):
        response = self.client.get(reverse('locations_api:countries/', kwargs={'country_id': random.randint(1, 30)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_city_get(self):
        response = self.client.get(reverse('locations_api:cities/', kwargs={'id': random.randint(10, 300)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
