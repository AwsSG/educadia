from django.contrib import admin
from .models import Donate


class DonateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'amount', 'date')

    readonly_fields = ('date', 'amount')


admin.site.register(Donate, DonateAdmin)
