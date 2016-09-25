from django.contrib import admin

# Register your models here.
from test_admin_panel.models import SimpleMoneyModel, SimpleMoneyModelProxy

# Writable admin pages
admin.site.register(SimpleMoneyModel)


# ReadOnly admin pages
@admin.register(SimpleMoneyModelProxy)
class ROAdmin(admin.ModelAdmin):
    readonly_fields = ['pay',]


