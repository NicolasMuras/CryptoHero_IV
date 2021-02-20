from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from transaction.models import Transaction

from transaction.api.serializers.transaction_serializers import TransactionSerializer


TRANSACTIONS_URL = reverse('transaction:transaction-list')


class TransactionApiTests(TestCase):
    # Testea

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_transaction(self):
        # Testea la devolución de un listado de objetos 'transaction'.

        # Creamos un objeto.
        Transaction.objects.create(
            sender = 'Nico',
            receiver = 'Agus',
            amount = 12.23,
            txhash = "string",
            timestamp = 1592830770594
        )
        # Hacemos GET a la URI especificada para obtener la 'data' almacenada y el status code.
        res = self.client.get(TRANSACTIONS_URL)
        transaction = Transaction.objects.all().order_by('-timestamp')

        # Utilizamos el objeto transaction para pasarlo al serializador y devolver un JSON.
        serializer = TransactionSerializer(transaction, many=True)

        # Comprobamos que el status sea 200.
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # Comprobamos que los datos devueltos en el GET Request y en el serializador sean los mismos.
        self.assertEqual(res.data, serializer.data)

    def test_create_transaction_successfull(self):
        # Testea que se cree con exito una nueva 'transaction'.

        # Realizamos un POST con el contenido de la var 'payload'.
        payload = {
            "currency": "Ethereum",
            "sender": 'Nico',
            "receiver": 'Agus',
            "amount": 12.23,
            "txhash": "string",
            "timestamp": 1592830770594
        }
        
        self.client.post(TRANSACTIONS_URL, payload)

        # Comprobación que devuelve un valor boolean si el objeto existe.
        exists = Transaction.objects.filter(
            txhash = payload['txhash']
        ).exists()

        # Comprobación final utilizando var 'exists'.
        self.assertTrue(exists)

    def test_create_transaction_invalid(self):
        # Testeamos la creación de una 'transaction' con un valor invalido.
        payload = {'txhash': ''}
        res = self.client.post(TRANSACTIONS_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
