from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet,ProductViewSet

router = routers.DefaultRouter()

router.register(r'category',CategoryViewSet,basename='category')
router.register(r'product',ProductViewSet,basename='product')

urlpatterns = [
    path('',include(router.urls)),
]