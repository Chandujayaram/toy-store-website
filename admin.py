from django.contrib import admin
from .models import Category, Toy, Cart, CartItem, Order, OrderItem

admin.site.register(Category)
admin.site.register(Toy)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
