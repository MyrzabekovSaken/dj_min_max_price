from django.urls import path, include
from rest_framework import routers
from .views import ProductList, ProductDetail

router = routers.DefaultRouter()
router.register('products', ProductList)

urlpatterns = [
    path('/', include(router.urls)),
]
