# Week 10 — Weather Dashboard with Chart.js

**Aim:** Create an application that fetches weather information from openweathermap.org and displays the current and historical weather as charts using Chart.js, implemented with Django.

## Project structure

```text
weather_project/
├── manage.py
├── .env
├── requirements.txt
├── weather_project/
│   ├── settings.py
│   └── urls.py
└── weather/
    ├── urls.py
    ├── views.py
    ├── services.py          # calls the OpenWeatherMap API
    ├── utils.py             # optional (from the manual)
    ├── models.py            # WeatherSnapshot
    ├── forms.py             # CityForm
    ├── templates/weather/dashboard.html
    └── static/weather/
        ├── styles.css
        └── charts.js
```

## Steps

1. **Get an API key.** Sign up free at openweathermap.org, then copy your key from *My API keys*. A new key can take an hour or two to start working.
2. **Create an environment, the project and the app:**

   ```bash
   python -m venv week10
   week10\Scripts\activate
   pip install django requests python-dotenv
   django-admin startproject weather_project
   cd weather_project
   python manage.py startapp weather
   ```

3. **Add the text files** next to `manage.py`: [requirements.txt](open:week10-weather-dashboard/weather_project/requirements.txt) and [.env](open:week10-weather-dashboard/weather_project/.env). Put your real key after `OPENWEATHER_API_KEY=`.
4. **Edit settings** in [weather_project/settings.py](open:week10-weather-dashboard/weather_project/weather_project/settings.py): load `.env` with `load_dotenv`, read `OPENWEATHER_API_KEY`, and add `"weather"` to `INSTALLED_APPS`.
5. **Map the URLs** in [weather_project/urls.py](open:week10-weather-dashboard/weather_project/weather_project/urls.py) (project) and [weather/urls.py](open:week10-weather-dashboard/weather_project/weather/urls.py) (app).
6. **Write the model** in [weather/models.py](open:week10-weather-dashboard/weather_project/weather/models.py). Each `WeatherSnapshot` row is one reading; together they are the history.
7. **Write the API calls** in [weather/services.py](open:week10-weather-dashboard/weather_project/weather/services.py): `get_current_weather()` uses `/data/2.5/weather`, `get_forecast_5day()` uses `/data/2.5/forecast` (3-hour steps for 5 days). The manual's [utils.py](open:week10-weather-dashboard/weather_project/weather/utils.py) does a simpler version of the first call.
8. **Write the form** in [weather/forms.py](open:week10-weather-dashboard/weather_project/weather/forms.py): a city box and an optional country code.
9. **Write the view** in [weather/views.py](open:week10-weather-dashboard/weather_project/weather/views.py). On submit it fetches current weather and the forecast, saves a snapshot, and loads the last 30 snapshots for that city.
10. **Create the template** [dashboard.html](open:week10-weather-dashboard/weather_project/weather/templates/weather/dashboard.html). `{{ forecast_points|json_script:"forecast-data" }}` safely hands the Python lists to JavaScript.
11. **Add the static files** [charts.js](open:week10-weather-dashboard/weather_project/weather/static/weather/charts.js) (draws four line charts with Chart.js) and [styles.css](open:week10-weather-dashboard/weather_project/weather/static/weather/styles.css). The manual's sample chart is kept as [weather_trends_demo.html](open:week10-weather-dashboard/weather_trends_demo.html) — open it directly to see Chart.js work with fixed data.
12. **Run the application:**

    ```bash
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

    Enter a city such as `Hyderabad` and press **Update**. Submit the same city a few times to build up the history chart.
