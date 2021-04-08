from django.contrib import admin
from .models import UserAccount
# Register your models here.


class UsersAccounts(admin.ModelAdmin):
    list_display = (
        'user',
        'first_names',
        'last_name',
        'user_type',
    )


admin.site.register(UserAccount, UsersAccounts)
