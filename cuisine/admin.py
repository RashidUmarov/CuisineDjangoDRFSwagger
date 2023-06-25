from django.contrib import admin

from .models import (
    Category, Dish
)

admin.site.register(Dish)


class DishInline(admin.TabularInline):
    model = Dish
    readonly_fields = ('id',)
    extra = 1
    classes = ('collapse',)
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishInline]
    fk_name = "category"
