from audioop import reverse
from urllib import response
from django.test import TestCase



class TestUrls(TestCase):
    def test_gallery_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
  
