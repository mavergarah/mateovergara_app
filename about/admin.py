from django.contrib import admin

# Register your models here.
from .models import AboutMV


@admin.register(AboutMV)
class AboutMVAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

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
