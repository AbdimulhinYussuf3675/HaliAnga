# class CityForm(forms.ModelForm):
#     class Meta:
#         model = OpenWeatherCity 
#         fields = ['name']
#         widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
class CityForm(forms.ModelForm):
    class Meta:
        model = OpenWeatherCity 
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
        for city in OpenWeatherCity.objects.filter(country="KE").order_by('name')[:1500]