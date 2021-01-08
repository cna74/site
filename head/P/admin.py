from django.contrib import admin
from .models import Filament, Category, FilamentImage


class FilamentImageAdmin(admin.StackedInline):
    model = FilamentImage


@admin.register(Filament)
class FilamentAdmin(admin.ModelAdmin):
    list_display = ("category", "type", "color", "qty", "price", "is_active")
    list_filter = ('category', 'type', 'color', 'is_active')

    inlines = [FilamentImageAdmin]

    class Meta:
        model = Filament


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass

