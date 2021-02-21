from rest_framework import serializers

from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('sender', 'receiver', 'amount', 'txhash', 'timestamp')
        read_only_fields = ('id',)