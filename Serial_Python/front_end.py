import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.constants import *
import serial.tools.list_ports


#Select the uart only whit serial tag
def list_serial_ports():
    try:
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            if("Serial" in desc):
                serial_devices = "{}".format(port)
        return(serial_devices)
    except (serial.SerialException , NameError):
        pass
        return("")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row = 0, column = 0 , sticky='nsew')
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Label(self)
        self.hi_there["text"] = "Select Serial Port:"
        self.hi_there.columnconfigure(0, weight=1)
        self.hi_there.rowconfigure(0, weight=1)
        self.hi_there.grid(row = 0, column = 0, padx=2, pady=2 , sticky="nsew") 
        
        self.combo = ttk.Combobox(self)
        self.combo["values"] = []
        self.combo["postcommand"] = self.select_port
        self.combo["state"] = "readonly"
        self.combo.grid(row = 0, column = 1, padx=2, pady=2, sticky="nsew")
        self.combo.columnconfigure(0, weight=1)
        self.combo.rowconfigure(0, weight=1)

        self.button_connect = tk.Button(self)
        self.button_connect["text"] = "Connect Port"
        self.button_connect["command"] = self.connect
        self.button_connect.columnconfigure(0, weight=1)
        self.button_connect.grid(row = 0, column = 2, padx=2, pady=2, sticky="nsew") 

        self.button_sel_files = tk.Button(self)
        self.button_sel_files["text"] = "Select File PATH"
        self.button_sel_files["command"] = self.select_file_path
        self.button_sel_files.columnconfigure(0, weight=1)
        self.button_sel_files.grid(row = 1, column = 0, sticky="nsew") 
        
        self.path_entry = tk.Entry(self)
        self.path_entry["width"] = 50
        self.path_entry.grid(row = 1, column = 1, columnspan=3, sticky="nsew") 

        self.button_save = tk.Button(self)
        self.button_save["text"] = "Save in .csv"
        self.button_save["command"] = self.save_csv
        self.button_save.grid(row = 2, column = 0, sticky="nsew")
        #Variables
        self.file_rute = tk.StringVar()
        self.name_file = tk.StringVar()
        serial_ports = []
        selected_port = ""

    def connect(self):
        selected_port = self.combo.get()
        print(self.combo.get())
    
    def select_port(self):
        serial_ports = serial.tools.list_ports.comports()
        self.combo["values"] = serial_ports

    def select_file_path(self):
        self.file_rute.set(filedialog.askdirectory())
        self.path_entry.insert(0, self.file_rute.get())
    
    def save_csv(self):
        with open("test.csv",'w',encoding = 'utf-8') as f:
            f.write("my first file\n")
            f.write("This file\n\n")
            f.write("contains three lines\n")

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
