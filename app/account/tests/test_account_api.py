from django.urls import reverse
from core.tests.test_api_abstract import ApiTests
from account.models import Account
from account.api.serializers.account_serializers import AccountSerializer


class AccountApiTests(ApiTests):

    url = reverse('account:account-list')
    Model = Account
    serializer_class = AccountSerializer

    def test_retrieve_object(self):

        self.Model.objects.create(
            currency='BTC',
            balance = 0.00366963
        )

        objeto = self.Model.objects.all().order_by('-id')

    def test_create_object_successfull(self):

        payload = {
            "currency": "Ethereum",
            "balance": 0.00157422
        }

        exists = self.Model.objects.filter(
            currency = payload['currency']
        ).exists()


    def test_create_object_invalid(self):
        payload = {'currency': ''}
