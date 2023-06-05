from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from network_links.models import Network, Product, Contacts


class ContactsTabular(admin.TabularInline):
    """Дополнительный модуль Контакты для админки"""
    model = Contacts
    extra = 1


class ProductTabular(admin.TabularInline):
    """Дополнительный модуль Продукция для админки"""
    model = Product
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Создание модели Продукция для админки'''
    list_display = ['title', 'model', 'release_date']
    ordering = ['title']
    search_fields = ('title', 'model')
    list_filter = ['title']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    '''Создание модели Контакты для админки'''
    list_display = ['email', 'country', 'city', 'street', 'number_house']
    search_fields = ('country', 'city')
    list_filter = ['email', 'country', 'city']


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    '''Создание модели Торговая сеть для админки'''

    list_display: list[str] = [
        'id',
        'name',
        'provider_url',
        'debt',
    ]
    list_display_links: list[str] = ['id', 'name']
    list_filter: tuple[str] = ('contacts__city',)
    actions: tuple[str] = ('set_debt_to_zero',)
    inlines = [ContactsTabular, ProductTabular]

    def provider_url(self, obj):
        """Получить адрес поставщика"""
        if obj.provider:
            url = reverse('admin:network_links_network_change', args=[obj.provider.id])
            return format_html(
                '<a href="{0}">{1}</a>', url, obj.provider)
        return "-"

    provider_url.short_description = 'Provider'

    @admin.action(description='Clear debt')
    def set_debt_to_zero(self, request, queryset):
        """Погошение задолжности поставшика"""
        queryset.update(debt=0)
        self.message_user(request, f"Задолженность погашена.")

