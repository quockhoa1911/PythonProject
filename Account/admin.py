from django.contrib import admin
from .models.Account import Account
from .models import Role

# Register your models here.
admin.site.register(Role)
admin.site.register(Account)
