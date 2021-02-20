from rest_framework import viewsets, mixins

from account.models import Account
from account.api.serializers import account_serializers


class AccountViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Account.objects.all()
    serializer_class = account_serializers.AccountSerializer