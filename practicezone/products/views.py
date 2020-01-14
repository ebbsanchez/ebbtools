from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import Group

from shopping_cart.models import Order
from .models import Product
from practicezone.extras import get_random_guest_user


def product_list(request):
    guest_group = Group.objects.get(name="Guests")
    user_groups = request.user.groups.all()

    if guest_group not in user_groups:
        guest = get_random_guest_user()
        login(request, guest)
    
    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(
        owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [
            product.product for product in user_order_items]

    context = {
        'username': request.user.username,
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "products/product_list.html", context)

def clear_books(request):
    profile = request.user.profile
    profile.ebooks.clear()
    profile.save()

    return redirect(reverse('products:product-list'))