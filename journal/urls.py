from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet,ProductViewSet

router = routers.DefaultRouter()

router.register('category',CategoryViewSet,basename='category')
router.register('product',ProductViewSet,basename='category')

urlpatterns = [
    path('',include(router.urls)),
]