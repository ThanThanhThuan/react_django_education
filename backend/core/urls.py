from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This prefixes all analytics URLs with 'api/'
    path('api/', include('analytics.urls')), 
]