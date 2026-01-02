from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducationViewSet

router = DefaultRouter()
# This registers the route 'education/'
router.register(r'education', EducationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]