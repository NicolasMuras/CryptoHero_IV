from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.api.urls')),
    path('api/transaction/', include('transaction.api.urls')),
    path('api/block/', include('block.api.urls')),
]
