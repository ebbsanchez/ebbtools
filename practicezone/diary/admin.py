from django.contrib import admin
from .models import Entry
# Register your models here.


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass
