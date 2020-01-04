from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication with rest_framework. Now we can login
    path('api/v1/base_auth/', include('rest_framework.urls')),
    path('api/v1/cars/', include('cars.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
]
