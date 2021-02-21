from rest_framework import viewsets, mixins

from block.models import Block
from block.api.serializers import block_serializers


class BlockViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin, 
                     mixins.CreateModelMixin):

    queryset = Block.objects.all()
    serializer_class = block_serializers.BlockSerializer

    def perform_create(self, serializer):
        # Crea un nueva 'block'.
        serializer.save()


