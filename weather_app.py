from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather App")
root.iconbitmap("taco1.ico")
root.geometry("400x60")
# root.configure(background = "green")

def zip_lookup():
    # zip.get()
    # zip_label = Label(root , text = zip.get())
    # zip_label.grid(row = 1, column = 0  , columnspace = 2)


# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=89C0897E-2BA1-4D11-94FA-0A0933AE9505
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=89C0897E-2BA1-4D11-94FA-0A0933AE9505")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_colour = "#00E400"
        elif category == "Moderate":
            weather_colour = "#FFFF00"
        elif category == "Unhealthy for Sensitive People":
            weather_colour = "#FF7E00"
        elif category == "Unhealthy":
            weather_colour = "#FF0000"
        elif category == "Very Unhealthy":
            weather_colour = "#8F3F97"
        elif category == "Hazardous":
            weather_colour = "#7E0023"

        my_label = Label(root, text=city + " Air Quality : " + str(quality) + " " + category, font=("Helvetica", 16), background = weather_colour)
        my_label.pack()
    except Exception as e:
        api = "Error.."


zip = Entry(root)
zip.grid(row = 0, column = 0 )
zip.pack()

zip_button = Button(root, text = "Lookup Zipcode" , command = zip_lookup)
zip_button.pack()

root.mainloop()
