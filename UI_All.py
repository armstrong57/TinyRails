"""
This module runs the GUI to display the information of all stations.
The elements of the GUI are as follows:
 - Header: a label with the column headers
 - Station List: a listbox where each row contains the information of a single station
 - Scrollbar: to scroll through the Station List
"""

import tkinter as tk
from tkinter import font
from UI_header import stations

# Initialize the window
window = tk.Tk()

# Initialize the scrollbar. It will be on the right hand side of the screen.
scroll = tk.Scrollbar(window)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Initialize the header.
station_header = tk.Label(
    window,
    text = "Station Name                 Region                     Resource                   Size   ",
    font = ('Courier New', '12'),
    width = 90,
    height = 1
)

# Initialize the Station List.
list_station = tk.Listbox(
    window,
    yscrollcommand = scroll.set,
    font = ('Courier New', '12'),
    width = 90,
    height = 40
)

# Set the format for each line of the Station List.
station_format = '{0:29} {1:25} {2:25} {3:2d}'

# Enter the stations into the Station List.
# Stations are obtained from the getStations() call in UI_header.
for station in stations:
    list_station.insert(tk.END, station_format.format(stations[station].name, stations[station].region, stations[station].resource, stations[station].size))

# Pack elements and final configuration.
station_header.pack()
list_station.pack(side=tk.LEFT, fill=tk.BOTH)
scroll.config(command = list_station.yview)

window.mainloop()
