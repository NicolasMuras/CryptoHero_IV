from django.test import TestCase
from django.contrib.auth import get_user_model

from account import models


def sample_user(email='test@email.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_account_str(self):
        # Se testea representación 'string' de account.
        account = models.Account.objects.create(
            currency='BTC',
            balance = 0.00366963,
            available = 0.00266963,
            balance_local = 38.746779155,
            available_local = 28.188009155,
            rate = 10558.77
        )

        self.assertEqual(str(account), account.currency)

        