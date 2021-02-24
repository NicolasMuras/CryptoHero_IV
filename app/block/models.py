from django.db import models

class Block(models.Model):

    id = models.AutoField(primary_key = True)
    status = models.BooleanField()
    merkle_root = models.CharField(max_length=64, null = True, blank = True, unique = True)
    block_hash = models.CharField(max_length=255, null = True, blank = True, unique = True)

    def __str__(self):
        return str(self.id)

    def transactions(self):
        if not hasattr(self, '_transactions'):
            self._transactions = self.transaction_set.all()
        return self._transactions