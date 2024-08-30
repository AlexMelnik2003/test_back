from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent')
    search_fields = ('name', 'menu_name')

admin.site.register(MenuItem, MenuItemAdmin)
