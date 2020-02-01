from django.contrib import admin
from . import models
# Register your models here.


class ChartItemInline(admin.TabularInline):
    model = models.ChartItem
    ordering = ['order']


@admin.register(models.FlowChart)
class FlowChartAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]
    inlines = [ChartItemInline]


class ChartItemAdmin(admin.ModelAdmin):
    list_display = ["title", "id", "belong"]


# admin.site.register(models.FlowChart)
admin.site.register(models.ChartItem, ChartItemAdmin)
