import requests


API_KEY = f"{Your_Api_key}"

ONE_CALL_API_ED = "https://api.openweathermap.org/data/2.5/onecall"

ACC_SID = "ACede475a60a45b483587ff7e9a4e71a11"
AUTH_TOK = "ed9e5394471fb6e748aea0dbd527e20b"

parameters = {
    "lat":40.7128,
    "lon":74.0060,
    "appid":API_KEY,
    "exclude":"current,minutely,daily"
}

response = requests.get(ONE_CALL_API_ED,params=parameters)
response.raise_for_status()
data = response.json()

print(data)
