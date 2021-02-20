from rest_framework import serializers

from account.models import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('currency', 'balance', 'available', 'balance_local', 'balance_local', 'available_local', 'rate')
        read_only_fields = ('id',)