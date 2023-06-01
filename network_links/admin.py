from django.contrib import admin

from network_links.models import Factory, Retail, Individual, Product


admin.site.register(Factory)
admin.site.register(Product)


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'provider', 'debt', 'country', 'city']
    list_editable = ['debt']
    ordering = ['-debt', 'city']
    search_fields = ('city',)
    list_filter = ('city',)


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ['name', 'provider', 'debt', 'country', 'city']
    list_editable = ['debt']
    ordering = ['-debt', 'city']
    search_fields = ('city',)
    list_filter = ('city',)

