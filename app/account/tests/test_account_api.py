from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from account.models import Account

from account.api.serializers.account_serializers import AccountSerializer

ACCOUNTS_URL = reverse('account:account-list')

class AccountApiTests(TestCase):
    # Testea

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_account(self):
        # Testea la devolución de un listado de objetos 'account'.

        # Creamos un objeto.
        Account.objects.create(
            currency='BTC',
            balance = 0.00366963,
            available = 0.00266963,
            balance_local = 38.746779155,
            available_local = 28.188009155,
            rate = 10558.77
        )
        # Hacemos GET a la URI especificada para obtener la 'data' almacenada y el status code.
        res = self.client.get(ACCOUNTS_URL)
        account = Account.objects.all().order_by('-currency')

        # Utilizamos el objeto account para pasarlo al serializador y devolver un JSON.
        serializer = AccountSerializer(account, many=True)

        # Comprobamos que el status sea 200.
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # Comprobamos que los datos devueltos en el GET Request y en el serializador sean los mismos.
        self.assertEqual(res.data, serializer.data)
