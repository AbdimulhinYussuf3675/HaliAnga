from django import forms
from django.contrib.auth.models import User
from .models import OpenWeatherCity

class UserRegistratinForm(forms.ModelForm):
    password = forms.CharField(label ='Password',
                                widget = forms.PasswordInput)

    password2 =forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'email')    
    
    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError(' YOUR PASSWORD DONT MATCH')
    
        return cd['password2']


class CityForm(forms.Form):
    city = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['city'] = forms.ChoiceField(
            choices=[
                (city.open_weather_id, city.name)
                for city in OpenWeatherCity.objects.filter(country="KE").order_by('name')[:1500]
            ]
        )


