from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    filter_horizontal = ["tags", ]

admin.site.register(Todo, TodoAdmin)
