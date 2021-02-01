import sys

#Configure buffers for serial
""" Buffer serial tx size """
BUFFER_SERIAL_TX_SIZE = 32
""" Buffer serial rx size """
BUFFER_SERIAL_RX_SIZE = 32
""" Data size in bytes """
DATA_SIZE = 4

#Configure serial data format
""" Buffer serial format  22 [Byte] """
BUFFER_SERIAL_FORMAT = 'f'

#Configure baudrate
BAUD_RATE = 115200

def list_serial_ports():
    import serial.tools.list_ports
    try:
        ports = serial.tools.list_ports.comports()
        print("List of connected Devices:")
        for port in ports:
            print(port)
        for port, desc, hwid in sorted(ports):
            if("Serial" in desc):
                serial_devices = "{}".format(port)
        print(serial_devices)
    except (serial.SerialException , NameError):
        print("Not found Serial Port in devices")
        sys.exit()
    return(serial_devices)

import serial
import time
import csv
from struct import unpack
import numpy as np


def read_serial( serial_devices ):
    #Funcion lamba, a la llamada devuelve el tiempo en ms
    current_milli_time = lambda: int(round(time.time() * 1000))
    #Variable de tiempo enlapsado para sincronizar
    time_enlapsed = current_milli_time()

    SerialPort = serial.Serial(serial_devices, baudrate=BAUD_RATE, timeout = None)
    #Buffer de entrada y de salida de 32bytes
    SerialPort.set_buffer_size(rx_size = BUFFER_SERIAL_RX_SIZE , tx_size = BUFFER_SERIAL_TX_SIZE) 
    array_out = np.empty([1,0], dtype=int)

    while True:
        try:
            line = SerialPort.read(DATA_SIZE)
            array_out = np.array([current_milli_time() - time_enlapsed], dtype=int) 
            print( np.append( array_out , unpack(BUFFER_SERIAL_FORMAT,line)) )
            SerialPort.reset_input_buffer()
        except KeyboardInterrupt:
            #Interrup serial data read whit keyboard interrupt crtl + c
            SerialPort.close()
            print("Keyboard Interrupt")
            break

    print("End of program")
    return()


if __name__ == "__main__":
    read_serial(list_serial_ports())
    


