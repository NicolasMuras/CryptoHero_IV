import hashlib

from rest_framework import serializers

from block.models import Block
from transaction.api.serializers.transaction_serializers import TransactionSerializer

#############################################[  GLOBALS  ]############################################

ADD_BLOCK = 'Se añadira el bloque {} a la blockchain.'.format(id)

def comprobar_espacio(value):
        # custom validation: El bloque admite un maximo de 4 transacciones.
        if value == 4:
            print(ADD_BLOCK)

######################################################################################################


class BlockSerializer(serializers.Serializer):

    status = serializers.BooleanField()
    merkle_root = serializers.CharField(max_length=64)
    block_hash = serializers.CharField(max_length=255)
    transactions = TransactionSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Block
        fields = ('id', 'status', 'merkle_root', 'block_hash', 'transactions')
        read_only_fields = ('id',)

class DetailBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = '__all__'
