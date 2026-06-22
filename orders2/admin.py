from django.contrib import admin
from .models import ChickenPart, Customer
# Register your models here.

@admin.register(ChickenPart)
class ChickenPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_kg', 'description')
    search_fields = ('name', 'description')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('restaurant_name', 'Name', 'mobile', 'email', 'created_at')
    search_fields = ('restaurant_name', 'Name', 'mobile', 'email')
