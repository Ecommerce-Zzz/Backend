from django.contrib import admin
from .models import Product


# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ["title", "owner", "price", "available", "created_at"]
    list_filter = ["created_at", "owner", "available"]
