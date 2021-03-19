import tkinter as tk
from tkinter import font
from UI_header import stations

window = tk.Tk()

scroll = tk.Scrollbar(window)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

list_station = tk.Listbox(
    window,
    yscrollcommand = scroll.set,
    font = ('Courier New', '12'),
    width = 90,
    height = 40
)

station_format = '{0:29} {1:25} {2:25} {3:2d}'

for station in stations:
    list_station.insert(tk.END, station_format.format(stations[station].name, stations[station].region, stations[station].resource, stations[station].size))
list_station.pack(side=tk.LEFT, fill=tk.BOTH)
scroll.config(command = list_station.yview)

window.mainloop()
