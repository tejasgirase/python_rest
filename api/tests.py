
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User

from django.test import TestCase
from .models import Bucketlist
from pprint import pprint
# Create your tests here.

class Modeltestcase(TestCase):

    def setUp(self):
        user = User.objects.create(username='nerd')
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name, owner=user)

    def test_model_can_create_bucketlist(self):
        
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        user = User.objects.create(username='nerd')
        self.bucketlist_data = {'name': 'Write world class code', 'owner': user.id}
        print(self.bucketlist_data)
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.responce = self.client.post(
            reverse('create'),
            self.bucketlist_data, 
            format='json')

    def test_api_can_create_a_bucketlist(self):
        self.assertEqual(self.responce.status_code, status.HTTP_201_CREATED)
    
    def test_authorization_is_enforced(self):
        new_client = APIClient()
        res = new_client.get('/bucketlists/', kwargs={'pk':3}, format='json')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_api_can_get_a_bucketlist(self):
        
        """Test the api can get a given bucketlist"""
        bucketlist = Bucketlist.objects.get()
        reponse = self.client.get(
            reverse('details', kwargs={'pk':bucketlist.id}), format="json"
        )
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        self.assertContains(reponse, bucketlist)

    def test_api_can_update_bucketlist(self):
        
        """test the api can update a given bucketlist"""
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'something new'}
        req = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(req.status_code, status.HTTP_200_OK)
    def test_api_can_delete_bucketist(self):
        
        """test the api can delete a bucketlist"""
        bucketlist = Bucketlist.objects.get()
        reponse = self.client.delete(
            reverse('details',kwargs={'pk':bucketlist.id}),
            format='json',
            follow=True
        )

        self.assertEqual(reponse.status_code, status.HTTP_204_NO_CONTENT)