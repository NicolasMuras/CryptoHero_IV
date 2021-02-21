from django.urls import path, include
from rest_framework.routers import DefaultRouter

from block.api.views import block_views

router = DefaultRouter()
router.register('blocks', block_views.BlockViewSet)

app_name = 'block'

urlpatterns = [
    path('', include(router.urls))
]