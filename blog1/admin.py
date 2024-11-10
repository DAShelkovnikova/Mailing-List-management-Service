from django.contrib import admin

from blog1.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "tittle", "published_date", "count_view")
    search_fields = ("tittle",)