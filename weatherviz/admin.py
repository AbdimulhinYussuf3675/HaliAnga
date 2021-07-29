from django.contrib import admin
from weatherviz.models import OpenWeatherCity


class OpenWeatherCityAdmin(admin.ModelAdmin):
    list_display = ("id", "open_weather_id", "name", "country")


admin.site.register(OpenWeatherCity, OpenWeatherCityAdmin)
