from django.contrib import admin
from django.contrib import messages
from rest_framework_api_key.models import APIKey


class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service', 'created', 'modified')

    fieldsets = (
        ('Required Information', {'fields': ('name', 'service')}),
        ('Additional Information', {'fields': ('key_message',)}),
    )

    search_fields = ('id', 'name',)

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return ['key_message']
        else:
            return ['key_message', 'service']

    def has_delete_permission(self, request, obj=None):
        return True

    def key_message(self, obj):
        if obj.key:
            return "Hidden"
        return "The API Key will be generated once you click save."

    def save_model(self, request, obj, form, change):
        if not change:
            messages.add_message(request, messages.WARNING, ('The API Key for %s is %s. Please note it since you will not be able to see it again.' % (obj.name, obj.key)))
        obj.save()


admin.site.register(APIKey, ApiKeyAdmin)
