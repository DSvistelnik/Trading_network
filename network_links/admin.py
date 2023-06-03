from django.contrib import admin

from network_links.models import Network, Product, Contacts


admin.site.register(Product)
#admin.site.register(Network)
admin.site.register(Contacts)

@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'provider', 'debt', 'country', 'city']
    #list_editable = ['debt']
    #ordering = ['-debt', 'city']
    #search_fields = ('city',)
    #list_filter = ('city',)



