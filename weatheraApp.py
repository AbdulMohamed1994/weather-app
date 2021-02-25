import tkinter
from tkinter import *
from tkinter import messagebox
import requests
from configparser import ConfigParser

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ba9c924cf7e0eef58a93818532d3d6f4'

def the_weather(area):
    results = requests.get(url.format(area, url))
    if results:
        json = results.json()
        area = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        celcius = temp_kelvin - 273.15
        fahrenheit = (temp_kelvin-273.15) * 9 / 5 + 32
        weather = json['weather'][0]['main']
        final = (area, country, celcius, fahrenheit, weather)
        return final
    else:
        return None


def search():
    city = city_txt.get()
    weather = the_weather(city)
    if weather:
        Location_1['text'] = '{}, {}'.format(weather[0], weather[1])
        Temp['text'] = '{:.2f}°C {:2f}°F'.format(weather[2], weather[3])
        weather['text'] = weather[5]
    else:
        messagebox.showerror('Error!', 'Place not found!')


root = Tk()
root.title("Weather App")

city_txt = StringVar()
city_e = Entry(root, textvariable=city_txt)
city_e.pack()

city_l1 = Label(root, text="Enter Your City")
city_l1.pack()

#Search Button
search_b1 = Button(root, text="Search", width=15, command=search)
search_b1.pack()

#Location
Location_1 = Label(root, text="Location", font=('bold', 20))
Location_1.pack()

#Temperature
Temp = Label(root, text="Temperature")
Temp.pack()

#Weather Output
Weather = Label(root, text="Weather")
Weather.pack()

root.geometry('250x150')
root.mainloop()