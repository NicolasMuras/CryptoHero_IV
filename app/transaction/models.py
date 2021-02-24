from django.db import models
from block.models import Block

class Transaction(models.Model):

    id = models.AutoField(primary_key = True)
    sender = models.CharField(max_length=255, null = False, blank = False, unique = True)
    receiver = models.CharField(max_length=255, null = False, blank = False, unique = True)
    amount = models.FloatField()
    timestamp = models.BigIntegerField()
    txhash = models.CharField(max_length=255, null = False, blank = False, unique = True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.amount = round(self.amount, 8)
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)