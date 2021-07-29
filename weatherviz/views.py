from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import requests
from django.conf import settings
from .forms import CityForm,UserRegistratinForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from  django.contrib import messages
from .models import Profile,OpenWeatherCity

def register(request):
    if request.method == 'POST':
        user_form = UserRegistratinForm(request.POST)
        
        if user_form.is_valid():
           
            new_user = user_form.save(commit= False)
           
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            Profile.objects.create(user= new_user)
            messages.success(request ,'Account created successfully')
            return redirect('city-weather')

        else:
            messages.error(request ,'Error creating your account')
            return render(request,'registration/register.html' , {'user_form':user_form,'messages':messages})


    else:
        user_form = UserRegistratinForm()

        return render(request,'registration/register.html' , {'user_form':user_form})



@login_required(login_url='login')
def view_weather_data_for_city(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_id = form.cleaned_data.get("city", 1273294)
            weather_data = get_weather_data_for_city(city_id=city_id)
    else:
        form = CityForm()
        weather_data = None

    return render(request,"weatherviz/index.html",{"weather_data": weather_data,"form": form})

import requests

from django.conf import settings


def get_weather_data_for_city(city_id):
    api_url = (
        settings.OPEN_WATHER_BASE_URL +
        f"weather?id={city_id}" +
        f"&appid={settings.OPEN_WEATHER_API_KEY}&units=metric"
    )
    resp = requests.get(api_url)
    return resp.json()
