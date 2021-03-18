import tkinter as tk

class UI_Button:
    def __init__(self, txt):
        self.text = txt
        self.widget = tk.Button(text=self.text, width=30, bg="blue", fg="yellow")
        

btn_curr = UI_Button("Current Stations")
btn_all = UI_Button("All Stations")
btn_lock = UI_Button("Locked Stations")
btn_cargo = UI_Button("Cargo")
btn_rsc_update = UI_Button("Update Station Resources")
btn_lvl_update = UI_Button("Upgrade Station")

buttons_dict = {
    "curr": btn_curr,
    "all": btn_all,
    "lock": btn_lock,
    "cargo": btn_cargo,
    "rsc": btn_rsc_update,
    "lvl": btn_lvl_update
}