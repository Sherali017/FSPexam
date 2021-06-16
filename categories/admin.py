from django.contrib import admin

from categories.models import CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    list_filter = ['title']





