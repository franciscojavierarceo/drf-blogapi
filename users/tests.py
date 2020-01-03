from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from .views import SignUpView
from django.urls import reverse
from django.test import Client
User=get_user_model()

class DetailTestCase(TestCase):
    
    def setUp(self):
        self.client=Client()
        self.factory=RequestFactory()
        self.user=User.objects.create(username='',email='sambo21@gmail.com', password='sambo21091992')

    def test_testing(self):
        
        request=self.factory.get('')
        request.user=self.user
        # if user.username is not None:
        #     response.status_code=404
        response=SignUpView.as_view()(request)
        self.assertEqual(response.status_code, 200)

class TestingCase(TestCase):

    def setUp(self):
        self.client=Client()

    def test_checkup(self):
        response=self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_verify_user_account(self):
        response=self.client.post('/accounts/signup/',{'email':'kakashi@gmail.com','password':'kakashi1234'})
        self.assertEqual(response.status_code, 200)

    def test_missMatch(self):
        response=self.client.post('/accounts/signup/',{'username': 'KaKa', 'email':'.com','password':'babi21091992'})
        self.assertEqual(response.status_code, 200)
    
