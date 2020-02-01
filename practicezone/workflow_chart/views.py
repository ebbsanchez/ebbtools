from django.shortcuts import render
from .models import FlowChart, ChartItem
# Create your views here.


def index(request):
    flow_charts = FlowChart.objects.all()
    context = {
        'flow_charts': flow_charts,
    }
    return render(request, 'workflow_chart/index.html', context)


def chart(request, chart_id):
    chart = FlowChart.objects.get(id=chart_id)
    chart_items = chart.chartitem_set.order_by('order')
    colors = ['red', 'blue', 'lime', 'teal', 'green']
    context = {
        'chart': chart,
        'chart_items': chart_items,
        'colors': colors,
    }
    return render(request, 'workflow_chart/chart.html', context)
