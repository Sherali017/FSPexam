from django.contrib import admin

from Newssite.models import NewsModel, ContactModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'created_at']
    list_display =  ['title', 'description', 'created_at']
    list_filter = ['title', 'created_at']
@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'created_at']







