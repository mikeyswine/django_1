from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    part_number = models.CharField(max_length=200, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    default_customer_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '1. Products'


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    inventory_available = models.IntegerField(null=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = '2. Product Inventories'


# Possible other models:
# Customer (which gets made whenever new Customer makes an account. Possibly customer logs in with this information)
# CustomerProduct (with specific price for that Customer)



