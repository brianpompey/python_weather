import tkinter as tk
import requests
import time

def getWeather():
    city = textfield.get()
    api = http://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid={d0c079a626b543e5ad861413e7c1e36e}
    json_data = requests.get(api).json()


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")


textfield = tk.Entry(canvas, font = t)
textfield.pack(pady=20)
textfield.focus()

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()


canvas.mainloop()