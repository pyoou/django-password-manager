from django.contrib import admin
from . import models as m


class SafeAdmin(admin.ModelAdmin):
    list_filter = [
        'id',
        'user',
        'purpose',
        'updated_at',
    ]

    list_display = ['id', 'user', 'purpose']

    list_per_page = 100


admin.site.register(m.Safe, SafeAdmin)
