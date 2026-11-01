# weather/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class WeatherSnapshot(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2, blank=True)  # e.g., "IN"
    timestamp = models.DateTimeField(auto_now_add=True)
    temp_c = models.FloatField(
        validators=[MinValueValidator(-100), MaxValueValidator(60)]
    )
    humidity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    wind_speed = models.FloatField(
        validators=[MinValueValidator(0)]
    )

    class Meta:
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["city"]),
            models.Index(fields=["timestamp"]),
        ]

    def __str__(self):
        return f"{self.city} ({self.country_code}) - {self.temp_c}°C at {self.timestamp:%Y-%m-%d %H:%M}"
