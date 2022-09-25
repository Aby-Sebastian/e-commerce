from django.test import TestCase

class SimpleTest(TestCase):
    def test_login(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)

    def test_register(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        response = self.client.get('/accounts/reset_password/')
        self.assertEqual(response.status_code, 200)

    def test_reset_password_sent(self):
        response = self.client.get('/accounts/reset_password_sent/')
        self.assertEqual(response.status_code, 200)

    def test_reset_password_complete(self):
        response = self.client.get('/accounts/reset_password_complete/')
        self.assertEqual(response.status_code, 200)