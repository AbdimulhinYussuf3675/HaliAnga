from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .services import get_weather_data_for_city
from .forms import CityForm,UserRegistratinForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from  django.contrib import messages


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
