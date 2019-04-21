
from rest_framework import status
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Bucketlist
# Create your tests here.

class Modeltestcase(TestCase):

    def setUp(self):

        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_bucketlist(self):
        
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.responce = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format='jason'
        )

    def test_api_can_create_a_bucketlist(self):
        self.assertEqual(self.responce.status_code, status.HTTP_201_CREATED)