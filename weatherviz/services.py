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
