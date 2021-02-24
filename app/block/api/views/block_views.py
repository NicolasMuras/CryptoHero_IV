from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins
from rest_framework.response import Response

from block.models import Block
from block.api.serializers.block_serializers import DetailBlockSerializer, BlockSerializer


class BlockViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin, 
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin):

    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def perform_create(self, serializer):
        # Crea un nuevo 'block'.
        serializer.save()

    def retrieve(self, request, pk=None):
        queryset = Block.objects.all()
        block = get_object_or_404(queryset, pk=pk)
        serializer = DetailBlockSerializer(block)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
