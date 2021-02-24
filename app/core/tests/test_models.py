from django.test import TestCase

from account.models import Account
from transaction.models import Transaction
from block.models import Block


class ModelTests(TestCase):

    def test_account_str(self):
        # Se testea representación 'string' de account.
        account = Account.objects.create(
            currency='BTC',
            balance = 0.00366963
        )

        self.assertEqual(str(account), account.currency)

        
    def test_transaction_str(self):
        
        transaction = Transaction.objects.create(
            sender = 'Nico',
            receiver = 'Agus',
            amount = 12.23,
            txhash = "string",
            timestamp = 1592830770594
        )

        self.assertEqual(str(transaction), transaction.txhash)

    def test_block_str(self):
        
        block = Block.objects.create(
            status = False,
            merkle_root = '',
            block_hash = ''
        )

        self.assertEqual(str(block), str(block.sequence_id))