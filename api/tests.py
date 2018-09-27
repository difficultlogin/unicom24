from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class PartnerApiTest(APITestCase):
    def setUp(self):
        group = Group(name='partner')
        user = User(username='partner1')

        user.save()
        group.save()

        group.user_set.add(user.id)

    def testAccess(self):
        token = Token.objects.get(user__username='partner1')

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = reverse('api-clients')
        response = client.get(url)

        self.assertEqual(response.status_code, 200)


class OrganizationApiTest(APITestCase):
    def setUp(self):
        group = Group(name='organization')
        user = User(username='organization1')

        user.save()
        group.save()

        group.user_set.add(user.id)

    def testAccess(self):
        token = Token.objects.get(user__username='organization1')

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = reverse('api-clients')
        response = client.get(url)
        self.assertEqual(response.status_code, 403)

        url = reverse('api-requests')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)