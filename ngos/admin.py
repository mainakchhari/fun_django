from django.contrib import admin
from ngos.models import Ngo


@admin.register(Ngo)
class NgoAdmin(admin.ModelAdmin):
    ...
