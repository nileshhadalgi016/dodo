import requests
import json
import pyttsx3
from wikipedia import summary
import webbrowser
from random import choice
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()
db = json.load(open("database/Instructions.json"))


def speak(ins):
    print(">> " + ins)
    engine.say(ins)
    engine.runAndWait()


def wiki(search):
    try:
        res = summary(search, sentences=3)
    except:
        res = "Internet issue or multiple match found"
    return res


def weather(city, state, api_key):
    try:
        api = f'http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=metric'
        weather_data = requests.get(api).json()
        temperature = weather_data['main']['temp']  # Exracting temperature
        wind_speed = weather_data['wind']['speed']  # Exracting wind speed
        humidity = weather_data['main']['humidity']  # Exracting humidity
        description = weather_data['weather'][0]['main']  # Exracting weather description
        data = f"\ntemperature:{temperature}\nwind speed:{wind_speed}km/hr\nhumidity:{humidity}\nwith :{description}"
    except:
        data = "Internet Issue"
    return data
