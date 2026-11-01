# weather/forms.py  (create this file)
from django import forms

# changed: the manual's CityForm was a dropdown filled from saved
# WeatherSnapshot rows, which is empty the first time you run the app.
# A text box lets you type any city.
class CityForm(forms.Form):
    city = forms.CharField(label="City", max_length=100)
    country_code = forms.CharField(label="Country code", max_length=2, required=False,
                                   help_text="Optional, e.g. IN")
