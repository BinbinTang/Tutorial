from django.contrib import admin
from transactions.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
              (None,    {'fields': ['name']}),
              ('Account information', {'fields': ['balance']}),
              ]
    
admin.site.register(User, UserAdmin)