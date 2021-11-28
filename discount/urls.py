from django.urls import path, include
from .views import DiscountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', DiscountViewSet, basename='discout')

urlpatterns = [
    path('', include(router.urls)),
]