from rest_framework import routers
from django.urls import path, include
from network_links.views import NetworkViewSet, ContactViewSet, ProductViewSet, NetworkDetailViewSet

router = routers.DefaultRouter()

router.register(r'networks', NetworkViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'products', ProductViewSet)
router.register(r'network_detail', NetworkDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
