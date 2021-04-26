from django.contrib import admin
from .models import Donate


class DonateAdmin(admin.ModelAdmin):
    fields = ('name', 'amount')

    readonly_fields = ('date',)


admin.site.register(Donate, DonateAdmin)
