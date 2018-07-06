from django.contrib import admin
from .models import Attribute
# Register your models here.


class AttributeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attribute, AttributeAdmin)
