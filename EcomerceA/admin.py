import imp
from django.contrib import admin
from .models import Product , Category,Cart ,Wishlist , Order,OrderItem,Profile

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
