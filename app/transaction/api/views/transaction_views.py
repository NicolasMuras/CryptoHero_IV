from rest_framework import viewsets, mixins

from transaction.models import Transaction
from transaction.api.serializers import transaction_serializers


class TransactionViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin, 
                     mixins.CreateModelMixin):

    queryset = Transaction.objects.all()
    serializer_class = transaction_serializers.TransactionSerializer

    def perform_create(self, serializer):
        # Crea una nueva 'transaction'.
        serializer.save()


