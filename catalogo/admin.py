from django.contrib import admin
from .models import Category, Flower

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_available')
    list_filter = ('is_available', 'category')
    search_fields = ('name',)
    list_editable = ('price', 'stock', 'is_available')