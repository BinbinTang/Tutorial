from django.contrib import admin
from transactions.models import Account, Transaction

# Register your models here.


class TransactionInline(admin.TabularInline):
    model = Transaction


class AccountAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['name']}),
        ('Account information', {'fields': ['balance']}),
    ]
    inlines = [TransactionInline]


admin.site.register(Account, AccountAdmin)
