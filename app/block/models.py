from django.db import models


class Block(models.Model):

    sequence_id = models.IntegerField()
    transaction_list = models.CharField(max_length=255, null = False, blank = True, unique = True)
    status = models.BooleanField()
    merkle_root = models.CharField(max_length=255, null = False, blank = True, unique = True)
    block_hash = models.CharField(max_length=255, null = False, blank = True, unique = True)

    def __str__(self):
        return str(self.sequence_id)