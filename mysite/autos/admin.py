from django.contrib import admin
from .models import Auto, Make


class AutoAdmin(admin.ModelAdmin):
    pass


class MakeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Auto)
admin.site.register(Make, MakeAdmin)
