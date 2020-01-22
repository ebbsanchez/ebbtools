from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.my_profile, name="profile"),
    path('login', views.create_session, name="login"),
    path('logout', views.destroy_session, name="logout"),
    path('register', views.register, name="register"),
    
]
