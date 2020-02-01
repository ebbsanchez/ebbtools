from django.db import models


class FlowChart(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.title


class ChartItem(models.Model):
    title = models.CharField(max_length=30)
    order = models.IntegerField()
    belong = models.ForeignKey(FlowChart, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
