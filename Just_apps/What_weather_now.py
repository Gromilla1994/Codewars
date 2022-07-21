import requests

city = input("В каком городе хотите узнать погоду?\n")

weather_parameters = {
    "0": "",
    "T": "",
    "M": "",
    "lang": "ru",
}

response = requests.get(f"https://wttr.in/{city}", params=weather_parameters)

print(response.text)
