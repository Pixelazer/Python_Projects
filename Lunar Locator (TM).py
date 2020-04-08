#
# *-=[LUNAR LOCATOR]=-*
# By Aryan takalkar
#
#

from tkinter import *
import json
import requests
from geopy.geocoders import Nominatim

output = 'Output.txt'
url = "https://google.com"

date = str(7/24/2019)
geolocator = Nominatim(user_agent="Lunar_Locator")

# Initializing tkinter window 
browser_window = Tk()
browser_window.title("Lunar Locator")
label1 = Label(browser_window, text= 'Enter the date - (MM/DD/YYYY)')
label2 = Label(browser_window, text= 'Enter your location - ')
entry1 = Entry(browser_window)
entry2 = Entry(browser_window)
text = Text(browser_window)
Credits = Label(browser_window, text= 'Made by Aryan Takalkar')
Dcredits = Label(browser_window, text= "Data credit to the US Navy")
text.delete(1.0, END)
text.insert(1.0, 'Please enter the date and location.')

# Defining 'go' and getting data
def go():
    location = geolocator.geocode(str(entry2.get()))
    url = "https://api.usno.navy.mil/rstt/oneday?" + "date=" + str(entry1.get()) + "&coords=" + str((location.latitude, location.longitude))# + "&body=moon"
    r = requests.get(url).json()
    pr = json.dumps(r, indent=4)
    text.delete(1.0, END)
    text.insert(1.0, pr)

# Creating tkinter window
entry1.insert(END, "")
button = Button(browser_window, text='Go', command = go)
label1.pack(side=TOP)
entry1.pack(side=TOP)
label2.pack(side=TOP)
entry2.pack(side=TOP)
button.pack(side=TOP)
text.pack(side=TOP)
Credits.pack(side=BOTTOM)
Dcredits.pack(side=BOTTOM)
browser_window.mainloop()
