import requests
import json
user = input("Enter the city name : ")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user}&units=metric&appid=4e0e205d5eaaffbc4f026a523b2d145f")
# print(response.status_code)
# print(response.json())


emoji = {'Cloudy': "☁️", 'Drizzle': "🌧️", 'Haze': "♾️", 'Clear': "☀️"}

data = (response.json()['main']['temp'])
print(f"Current Temperature of {user.upper()} is : {data}°C")

climate = response.json()['weather'][0]['main']
if response.json()['weather'][0]['main'] == "Clouds":
    print(f"Weather of {user.upper()} is : {climate} {emoji['Cloudy']}")
elif response.json()['weather'][0]['main'] == "Drizzle" or "Rain":
    print(f"Weather of {user.upper()} is : {climate} {emoji['Drizzle']}")
elif response.json()['weather'][0]['main'] == "Haze":
    print(f"Weather of {user.upper()} is : {climate} {emoji['Haze']}")
elif response.json()['weather'][0]['main'] == "Clear":
    print(f"Weather of {user.upper()} is : {climate} {emoji['Clear']}")
else:
    print(f"Weather of {user.upper()} is : {climate}")
