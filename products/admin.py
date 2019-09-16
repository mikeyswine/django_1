from django.contrib import admin
from products.models import Product, Inventory
# If Pycharm cannot understand where to see the modules, it can sometimes be because the
# Project Structure has the wrong Content Root.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'part_number', 'cost', 'default_customer_price', 'active')
    search_fields = ['name', 'part_number', 'active']


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'inventory_available')


admin.site.register(Product, ProductAdmin)
admin.site.register(Inventory, InventoryAdmin)

