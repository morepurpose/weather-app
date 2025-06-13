import requests
import tkinter as tk
from tkinter import messagebox

# Replace this with your actual OpenWeatherMap API key
API_KEY = "9bf512e13997106bd925dff46e6b9ec3"

def get_weather(city):
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = (
            f"Weather in {city_name}, {country}\n"
            f"Temperature: {temperature}°C\n"
            f"Condition: {description}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        result_label.config(text=result)
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found or API issue.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
app = tk.Tk()
app.title("Weather Application")
app.geometry("400x300")
app.resizable(False, False)

city_label = tk.Label(app, text="Enter City:", font=("Arial", 14))
city_label.pack(pady=10)

city_entry = tk.Entry(app, font=("Arial", 14))
city_entry.pack(pady=5)

search_button = tk.Button(app, text="Get Weather", font=("Arial", 14),
                          command=lambda: get_weather(city_entry.get()))
search_button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

app.mainloop()

