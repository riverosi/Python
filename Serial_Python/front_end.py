import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

serial_ports = []

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Label(self)
        self.hi_there["text"] = "Select Serial Port:"
        self.hi_there.pack(side=tk.LEFT)

        self.button_connect = tk.Button(self)
        self.button_connect["text"] = "Click me"
        self.button_connect["command"] = self.say_hi
        self.button_connect.pack(side=tk.RIGHT)
        
        self.combo = ttk.Combobox(self)
        self.combo["values"] = []
        self.combo["postcommand"] = self.select_port
        self.combo["state"] = "readonly"
        self.combo.pack(side=tk.RIGHT)
        

    def say_hi(self):
        print("Connect!")
        print(self.combo.get())
    
    def select_port(self):
        serial_ports = serial.tools.list_ports.comports()
        self.combo["values"] = serial_ports

# create the application
root = tk.Tk()
#
# here are method calls to the window manager class
#
app = Application(master=root)
app.master.title("Serial Reader")
app.master.geometry("500x200")
# start the program
app.mainloop()
