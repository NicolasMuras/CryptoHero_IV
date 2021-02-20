from django.db import models


class Account(models.Model):

    currency = models.CharField(max_length=50)
    balance = models.FloatField()
    available = models.FloatField()
    balance_local = models.FloatField()
    available_local = models.FloatField()
    rate = models.FloatField()

    def save(self, *args, **kwargs):
        self.balance = round(self.balance, 8)
        self.available = round(self.available, 8)
        self.balance_local = round(self.balance_local, 9)
        self.available_local = round(self.available_local, 9)
        self.rate = round(self.rate, 2)
        super(Account, self).save(*args, **kwargs)

    def __str__(self):
        return self.currency