from django.contrib import admin
from .models import Todo, Category


class TodoAdmin(admin.ModelAdmin):
    filter_horizontal = ["tags", ]
    list_display = ["title", "category", "status"]
    list_filter = ["status", "category"]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)
