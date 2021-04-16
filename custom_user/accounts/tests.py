from django.test import TestCase
# from .model import CustomUser
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):

	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(
		username='suraj',
		email='srjthapa53@gmail.com',
		password='test123'
		)
		self.assertEqual(user.username, 'suraj')
		self.assertEqual(user.email, 'srjthapa53@gmail.com')
		