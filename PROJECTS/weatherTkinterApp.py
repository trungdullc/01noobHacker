"""
Main Purpose:
   Learn about base URL for API
   How to use python with API with no authentication

Idea stolen from:
   https://pythongeeks.org/python-live-weather-desktop-notifications/

Level: Intermediate
What I learned:
   When working with API most the time need import requests
   https://openweathermap.org/api
   from plyer import notification

Created by HackerDu
"""

import sys, time, requests                  # request module important for retreiving http without using curl or wget
from tkinter import *
from tkinter import messagebox as mb
try:
   from plyer import notification          # notification module
except ImportError:
   print("pip3 install plyer")

class Weather:
   def getNotification(self):
      """"
      Function to get notification of weather report from API: https://openweathermap.org/api
      """

      city_name = place_entry.get()
      baseUrl = "http://api.openweathermap.org/data/2.5/weather?"     # base url from API where can extract weather report

      try:
         complete_url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
         response = requests.get(complete_url)                       # requesting content of the url
         response_json = response.json()                             # converting response into json 
         response_column = response_json["main"]                     # getting "main" key from the json object
   
         temp_column = response_column["temp"]
         temp_column -= 273                                          # converting temperature from kelvin to celcius
         pressure_column = response_column["pressure"]
         humidity_column = response_column["humidity"]
         weather_column = response_json["weather"]
         weather_description = weather_column[0]["description"]

         # Combining above values as a string
         info = "Here is the eather description of "+ city_name+ ":"+" \nTemperature = " +str(temp_column) +"°C"+"\n atmospheric pressure = " + str(pressure_column) + "hPa"+"\n humidity = " +str(humidity_column) +"%"+"\n description of the weather= " + str(weather_description)

         # Showing notification 
         notification.notify(title = "YOUR WEATHER REPORT", message=info, timeout=2)

         time.sleep(7)    
      except Exception as e:
         mb.showerror('Error',e)

def main():
   global place_entry

   weather = Weather()

   root_window = Tk()
   root_window.title("Weather Desktop Notifier")
   root_window.geometry('700x200')
   root_window.config(bg='azure')
   root_window.resizable(width=0, height=0)

   Label(root_window, text="Weather Desktop Notifier", font=('Courier', 15), fg='grey19',bg='azure').place(x=100,y=15)
   Label(root_window, text='Enter the Location:', font=("Courier", 13),bg='azure').place(relx=0.05, rely=0.3)

   place_entry = StringVar(master=root_window)
   Entry(master=root_window, width=50, textvariable=place_entry).place(relx=0.5, rely=0.3)

   Button(root_window, text='Get Notification', font=7, fg='grey19',command=weather.getNotification).place(relx=0.4, rely=0.75)

   root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()