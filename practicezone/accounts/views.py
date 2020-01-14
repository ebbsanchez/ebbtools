from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from shopping_cart.models import Order
from .models import Profile


# Create your views here.
def my_profile(request):
    my_user_proile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_proile)
    context = {
        'my_orders': my_orders
    }

    return render(request, "Profile.html", context)
