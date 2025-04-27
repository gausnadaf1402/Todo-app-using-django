from django.contrib import admin
from .models import ToDo

# Register your models here.
class todoAdmin(admin.ModelAdmin):
    list_display=('title','date','user')
    search_fields=('title',)
    list_filter=('title','date')
admin.site.register(ToDo,todoAdmin)
