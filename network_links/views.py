from rest_framework import viewsets
from network_links.filters import CountryFilter
from network_links.models import Product, Network, Contacts
from network_links.permissions import IsActivePermission
from network_links.serializers import NetworkSerializer, ContactSerializer, ProductSerializer, \
    NetworkDetailSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    """ Представление для работы с торговой сетью"""
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActivePermission]

#Запрет обновления через API поля «Задолженность перед поставщиком»
    def perform_update(self, serializer):
        serializer.validated_data.pop('debt', None)
        super().perform_update(serializer)


class ContactViewSet(viewsets.ModelViewSet):
    """Представление для работы с контактами"""
    queryset = Contacts.objects.all()
    permission_classes = [IsActivePermission]
    serializer_class = ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Представление для работы с продукцией торговой сети"""
    queryset = Product.objects.all()
    permission_classes = [IsActivePermission]
    serializer_class = ProductSerializer


class NetworkDetailViewSet(viewsets.ModelViewSet):
    """Представление для торговой сети с контактами и продукцией данной торговой сети"""
    queryset = Network.objects.all()
    serializer_class = NetworkDetailSerializer
    permission_classes = [IsActivePermission]
    filterset_class = CountryFilter

    def perform_update(self, serializer):
        serializer.validated_data.pop('debt', None)
        super().perform_update(serializer)


