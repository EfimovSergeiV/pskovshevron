from django.contrib import admin
from main.models import ContactsModel


class SiteSettingsAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        # Запрещаем добавление нового объекта, если он уже существует
        if ContactsModel.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Запрещаем удаление объекта
        return False
    

admin.site.register(ContactsModel, SiteSettingsAdmin)