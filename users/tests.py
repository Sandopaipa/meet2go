from django.test import TestCase
from .models import AccountData


class AccountDataTestCase(TestCase):
    def setUp(self):
        self.account = AccountData.objects.create_user(
            email='TestUser@test.com',
            password='rgm4@c9$(L)_',
            first_name='TestUser',
            last_name='TestUser',
            birthdate='2001-01-01'
        )
        self.account.save()

    def tearDown(self):
        self.account.delete()

    def test_account_created(self):
        account = AccountData.objects.get(email='TestUser@test.com')
        self.assertIsNotNone(obj=account)
