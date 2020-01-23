from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.auth import get_user, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib import messages
from django import forms

from shopping_cart.models import Order
from .models import Profile
from django.contrib.auth.decorators import login_required

import datetime
import pytz

# Profile for shopping cart.

@login_required
def my_profile(request):
    user = get_user(request)
    username = user.get_username()
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    age = (user.date_joined - utc_now)
    age_in_day = age.days * -1
    my_user_proile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_proile)
    context = {
        'my_orders': my_orders,
        'user': user,
        'username': username,
        'age_in_day': age_in_day,
    }

    return render(request, "accounts/profile.html", context)

# Use Authentication


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile created.')
            return redirect('accounts:profile')
        else:
            context = {
                'form': form,
            }
            return render(request, 'accounts/register.html', context)
    else:
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/register.html', context)


def create_session(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        else:
            form = AuthenticationForm(request.POST)
            context = {
            'form': form,
            }
            messages.error_message = 'Unvalid username/<password></password>'
        return render(request, 'accounts/login.html', context)
    else:
        form = AuthenticationForm()
        context = {
        'form': form,
        }
        return render(request, 'accounts/login.html', context)

def destroy_session(request):
    logout(request)
    return redirect('accounts:profile')

def edit(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return


    return


def destroy():
    return
