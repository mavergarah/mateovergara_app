from django.contrib import admin
from django.db import models

# Register your models here.
from .models import AboutApp
from mdeditor.widgets import MDEditorWidget

@admin.register(AboutApp)
class AboutAppAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    description = {
        models.TextField:{'widget': MDEditorWidget}
    }

    list_display = (
        'title',
        'description'
    )

    fieldsets = (
        ('about item', {
            'fields': (
                'title',
                'description'
            ),
        }),
    )
