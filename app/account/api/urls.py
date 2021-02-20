from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.api.views import account_views

router = DefaultRouter()
router.register('accounts', account_views.AccountViewSet)

app_name = 'account'

urlpatterns = [
    path('', include(router.urls))
]