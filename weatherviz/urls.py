from django.contrib import admin
from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.view_weather_data_for_city, name="city-weather"),
    url(r'^register/', views.register,name = 'register'),
    url(r'^login/' , auth_views.LoginView.as_view() ,name ='login'),
    url(r'^logout/' , auth_views.LogoutView.as_view(),{"next_page": '/'} ,name ='logout' ),
]
