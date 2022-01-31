
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase


class ClientTests(APITestCase):
    def create_Client(self, first_name,last_name,gender,address,client):
        url = reverse('Client_list')
        data = {'first_name':first_name,
                'last_name': last_name,
                'gender': gender,
                'address': address,
                }
        response =  client.post(url,data,format='json')
        return response

    def test_post_Client(self):
        user = User.objects.create_superuser(
            'admin','admin@admin.pl','admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        new_first_name = 'Kamil'
        new_last_name = 'Tracz'
        new_gender = 'M'
        new_address = 'Kopernika 23'
        response = self.create_Client(
            new_first_name,new_last_name,new_gender,new_address,client)
        assert response.status_code == status.HTTP_201_CREATED


class alcoholCategoryTests(APITestCase):
    def create_alcoholCategory(self, name,client):
        url = reverse('alcoholCategory_list')
        data = {'name':name,
                }
        response =  client.post(url,data,format='json')
        return response

    def test_post_alcoholCategory(self):
        user = User.objects.create_superuser(
            'admin','admin@admin.pl','admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        new_name = 'whisky'
        response = self.create_alcoholCategory(
            new_name,client)
        assert response.status_code == status.HTTP_201_CREATED


