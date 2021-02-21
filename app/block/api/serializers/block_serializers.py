import hashlib

from rest_framework import serializers

from block.models import Block


class BlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = ('sequence_id', 'transaction_list', 'status', 'merkle_root', 'block_hash')
        read_only_fields = ('id',)