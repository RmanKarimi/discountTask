from django.contrib import admin
from .models import Store, DiscountType, Discount

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(DiscountType)
class DiscountTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('name', 'value', 'type')
    list_filter = ('value', 'type')
    search_fields = ('name', 'value')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('code', 'create_date', 'end_date', 'store', 'status')
    list_filter = ('store', 'status')
    search_fields = ('create_date', 'end_date')