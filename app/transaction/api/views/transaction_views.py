from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Count
from transaction.models import Transaction
from transaction.api.serializers.transaction_serializers import TransactionSerializer, DetailTransactionSerializer

class HelperTransactionAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin, 
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        # Crea una nueva 'transaction'.
        serializer.save()

    def retrieve(self, request, pk=None):
        queryset = Transaction.objects.all()
        transaction = get_object_or_404(queryset, pk=pk)
        serializer = DetailTransactionSerializer(transaction)
        return Response(serializer.data)

    def perform_destroy(self, serializer):
        serializer.delete()