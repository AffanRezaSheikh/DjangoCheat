# weather/utils.py
# From the manual (Step 3). The final views use services.py instead,
# so this file is optional.
import requests
from django.conf import settings

def fetch_weather(city, country_code="IN"):
    api_key = settings.OPENWEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return {
        "city": city,
        "country_code": country_code,
        "temp_c": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }
