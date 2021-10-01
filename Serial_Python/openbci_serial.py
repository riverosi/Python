import sys
import serial
import time
from struct import pack
import numpy as np

#Configure buffers for serial
""" Buffer serial tx size """
BUFFER_SERIAL_TX_SIZE = 512
""" Buffer serial rx size """
BUFFER_SERIAL_RX_SIZE = 512


#Configure baudrate
BAUD_RATE = 921600

buffer_data = bytearray(33)

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
        serial_devices = ""
        print("Not found Serial Port")
    return(serial_devices)

#para convertir de complemento a2 a counts de datos para los 8 canales de eeg
def array_convert(bytes_array):
    counts_channel = []
    counts_channel.append(int.from_bytes(bytes_array[1:3], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[4:6], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[7:9], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[10:12], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[13:15], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[16:18], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[19:21], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[22:24], byteorder='big',signed=True))
    return counts_channel
    

def read_serial():
    # Serial port obj
    SerialPort = serial.Serial(list_serial_ports(), baudrate=BAUD_RATE, timeout = None)
    #Buffer de entrada y de salida
    SerialPort.set_buffer_size(rx_size = BUFFER_SERIAL_RX_SIZE , tx_size = BUFFER_SERIAL_TX_SIZE)
    print("App is runing!!!")

    while '0xA0' == SerialPort.read():
        buffer_data = SerialPort.read_until(terminator='0xc0' ,size= len(buffer_data)-1)
        print(buffer_data)
        print(array_convert(buffer_data))
    
if __name__ == "__main__":
    read_serial()