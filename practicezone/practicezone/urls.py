"""practicezone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import todolist.views
from . import views

# from .views import testing_page

urlpatterns = [
    path('', views.index, name="homepage"),
    path('test', views.showTheTestResult, name='test'),
    path('todoapp/', todolist.views.index, name="todolist"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('products/', include('products.urls', namespace='products')),
    path('shopping_cart/', include('shopping_cart.urls',
                                   namespace='shopping_cart')),
    path('workflow_chart/', include('workflow_chart.urls',
                                    namespace='workflow_chart')),
    path('gitlog/', include("gitlog.urls", namespace='gitlog')),
]
