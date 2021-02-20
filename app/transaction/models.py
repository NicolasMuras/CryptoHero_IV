from django.db import models


class Transaction(models.Model):

    sender = models.CharField(max_length=255, null = False, blank = False, unique = True)
    receiver = models.CharField(max_length=255, null = False, blank = False, unique = True)
    amount = models.FloatField()
    txhash = models.CharField(max_length=255, null = False, blank = False, unique = True)
    timestamp = models.BigIntegerField()

    def save(self, *args, **kwargs):
        self.amount = round(self.amount, 8)
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return self.txhash