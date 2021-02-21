from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from transaction.models import Transaction
from transaction.api.serializers.transaction_serializers import TransactionSerializer


# Clase abstracta que proporciona una base para la realización de algunos test unitarios basicos.
# Nota: Se proporciona 'transactions' como test unitario base.
# Luego se sobreescriben los valores para cada objeto correspondiente.
class ApiTests(TestCase):

    # Para utilizar correctamente esta clase deberas sobreescribir estos tres valores.
    url = reverse('transaction:transaction-list')
    Model = Transaction
    serializer_class = TransactionSerializer

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_object(self):
        # Testea la devolución de un listado de objetos.

        # Creamos un objeto.
        self.Model.objects.create(
            sender = 'Nico',
            receiver = 'Agus',
            amount = 12.23,
            txhash = "string",
            timestamp = 1592830770594
        )

        # Hacemos GET a la URI especificada para obtener la 'data' almacenada y el status code.
        response = self.client.get(self.url)
        objeto = self.Model.objects.all().order_by('-id')

        # Utilizamos el objeto para pasarlo al serializador y devolver un JSON.
        serializer = self.serializer_class(objeto, many=True) 

        # Comprobamos que el status sea 200.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Comprobamos que los datos devueltos en el GET Request y en el serializador sean los mismos.
        self.assertEqual(response.data, serializer.data)

    def test_create_object_successfull(self):
        # Testea que se cree con exito un nuevo objeto.

        # Realizamos un POST con el contenido de la var 'payload'.
        payload = {
            "sender": 'Nico',
            "receiver": 'Agus',
            "amount": 12.23,
            "txhash": "string",
            "timestamp": 1592830770594
        }
        
        self.client.post(self.url, payload)

        # Comprobación que devuelve un valor boolean si el objeto existe.
        exists = self.Model.objects.filter(
            txhash = payload['txhash']
        ).exists()

        # Comprobación final utilizando var 'exists'.
        self.assertTrue(exists)

    def test_create_transaction_invalid(self):
        # Testeamos la creación de una 'transaction' con un valor invalido.
        payload = {'txhash': ''}
        response = self.client.post(self.url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
