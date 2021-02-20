from django.urls import path, include
from rest_framework.routers import DefaultRouter

from transaction.api.views import transaction_views

router = DefaultRouter()
router.register('transactions', transaction_views.TransactionViewSet)

app_name = 'transaction'

urlpatterns = [
    path('', include(router.urls))
]