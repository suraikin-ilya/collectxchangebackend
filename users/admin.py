from django.contrib import admin

# Register your models here.

from .models import User, Collection, Category, Preservation, Country, Item

class UserAdmin(User):
    list_display = ['id', 'nickname', 'email']
    list_filter = ['id','nickname', 'email']
    search_fields = ['nickname', 'email']

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'visibility', 'owner', 'views', 'created_date']
    list_filter = ['views','id','visibility', 'created_date']
    search_fields = ['name', 'description', 'owner']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']

@admin.register(Preservation)
class PreservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['code', 'name']

# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ['id', 'owner', 'name', 'category']
#     list_filter = ['id', 'category']
#     search_fields = ['name', 'category']

    # list_filter = ['id', 'category', 'trade', 'visibility']
    # list_display = ['id', 'owner', 'name', 'category', 'trade', 'visibility', 'date_create', 'collection']