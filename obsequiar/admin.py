from django.contrib import admin
from .models import Category, Product, Client, Order, OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(OrderItem)



