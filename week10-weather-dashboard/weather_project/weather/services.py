# weather/services.py  (create this file)
import requests
from django.conf import settings

BASE_URL = "https://api.openweathermap.org/data/2.5"
API_KEY = settings.OPENWEATHER_API_KEY

def get_current_weather(city: str, country_code: str = ""):
    if not API_KEY:
        raise RuntimeError("Missing OPENWEATHER_API_KEY")
    q = f"{city},{country_code}" if country_code else city
    url = f"{BASE_URL}/weather"
    params = {"q": q, "appid": API_KEY, "units": "metric"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    return {
        "city": data["name"],
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"],
        "temp_c": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"].title(),
        "icon": data["weather"][0]["icon"],
    }

def get_forecast_5day(city: str, country_code: str = ""):
    if not API_KEY:
        raise RuntimeError("Missing OPENWEATHER_API_KEY")
    q = f"{city},{country_code}" if country_code else city
    url = f"{BASE_URL}/forecast"
    params = {"q": q, "appid": API_KEY, "units": "metric"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    points = []
    for item in data.get("list", []):
        points.append({
            "dt_txt": item["dt_txt"],
            "temp_c": item["main"]["temp"],
            "humidity": item["main"]["humidity"],
            "wind_speed": item["wind"]["speed"],
        })
    return points
