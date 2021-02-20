from django.db import models


class Account(models.Model):

    currency = models.CharField(max_length=50)
    balance = models.FloatField()


    def save(self, *args, **kwargs):
        self.balance = round(self.balance, 8)
        super(Account, self).save(*args, **kwargs)

    def __str__(self):
        return self.currency