from django.conf.urls import url
from django.urls import path

from .views import product_list, clear_books


app_name = 'products'

urlpatterns = [
    path('clear', clear_books, name="clear"),
    url(r'^', product_list, name='product-list'),
]
