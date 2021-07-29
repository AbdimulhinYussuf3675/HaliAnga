import json
from django.core.management.base import BaseCommand, CommandError

from weatherviz.models import OpenWeatherCity


class Command(BaseCommand):
    help = "Load open weather city data from JSON file"

    def handle(self, *args, **kwargs):
        with open("weatherviz/data/city.list.json", "r") as f:
            city_list = json.loads(f.read())

        for city in city_list:
            ow_city_id = city["id"]

            OpenWeatherCity.objects.update_or_create(
                open_weather_id=ow_city_id,
                defaults={
                    "name": city["name"],
                    "country": city["country"],
                }
            )

        self.stdout.write(self.style.SUCCESS("Successfully loaded data from JSON file."))
