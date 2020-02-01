from django.urls import path
from . import views

app_name = 'workflow_chart'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:chart_id>', views.chart, name='chart'),
]
