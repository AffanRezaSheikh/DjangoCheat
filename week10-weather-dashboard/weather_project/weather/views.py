# weather/views.py
# changed: the manual's weather_chart_view rendered "weather/chart.html",
# but urls.py imports "dashboard" and dashboard.html expects current,
# forecast_points and historical_points. This view supplies exactly those.
import requests
from django.contrib import messages
from django.shortcuts import render
from django.utils.timezone import localtime
from .forms import CityForm
from .models import WeatherSnapshot
from .services import get_current_weather, get_forecast_5day

def dashboard(request):
    current = None
    forecast_points = []
    historical_points = []

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"].strip()
            country_code = form.cleaned_data["country_code"].strip().upper()
            try:
                current = get_current_weather(city, country_code)
                forecast_points = get_forecast_5day(city, country_code)

                # Save a snapshot so the "historical" chart grows each time
                WeatherSnapshot.objects.create(
                    city=current["city"],
                    country_code=country_code,
                    temp_c=current["temp_c"],
                    humidity=current["humidity"],
                    wind_speed=current["wind_speed"],
                )
            except RuntimeError as e:
                messages.error(request, str(e))
            except requests.RequestException:
                messages.error(request, f"Could not get weather for '{city}'. Check the city name and your API key.")

            if current:
                qs = WeatherSnapshot.objects.filter(city=current["city"]).order_by("-timestamp")[:30]
                historical_points = [
                    {
                        "time": localtime(s.timestamp).strftime("%Y-%m-%d %H:%M"),
                        "temp_c": s.temp_c,
                        "wind_speed": s.wind_speed,
                    }
                    for s in reversed(list(qs))
                ]
    else:
        form = CityForm()

    return render(request, "weather/dashboard.html", {
        "form": form,
        "current": current,
        "forecast_points": forecast_points,
        "historical_points": historical_points,
    })
