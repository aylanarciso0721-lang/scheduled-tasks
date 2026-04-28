import smtplib
import os
import requests

MY_EMAIL = "aylaparayno@gmail.com"
MY_PASSWORD = os.environ.get("AUTH_TOKEN")
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": -42.884140,
    "lon": 147.330228,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP('smtp.gmail.com', port=25) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Umbrella\n\n{"It is going to rain after a few hours. Don't forget to bring an umbrella."}"
        )
