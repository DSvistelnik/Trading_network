from rest_framework import serializers
from network_links.models import Network, Contacts, Product


class NetworkSerializer(serializers.ModelSerializer):
    """Сериалиалайзер для платформы торговой сети"""
    class Meta:
        model = Network
        fields = ['id', 'name', 'link', 'provider', 'debt', 'time']


class ContactSerializer(serializers.ModelSerializer):
    """Сериалиалайзер для работы с контактами звеньев"""
    trading_title = serializers.SerializerMethodField()

    class Meta:
        model = Contacts
        fields = ['id', 'email', 'country', 'city', 'street', 'number_house', 'trading', 'trading_title']

    def get_trading_title(self, obj):
        return obj.trading.title


class ProductSerializer(serializers.ModelSerializer):
    """Сериалиалайзер для работы с продукцией торговых сетей"""
    trading_title = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'model', 'release_date', 'trading', 'trading_title']

    def get_trading_title(self, obj):
        return obj.trading.title


class NetworkDetailSerializer(serializers.ModelSerializer):
    """Сериалиалайзер для торговой сети с контактами и продукцией торговой сети"""
    contacts = ContactSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Network
        fields = ['id', 'name', 'link', 'provider', 'debt', 'time', 'contacts', 'products']

