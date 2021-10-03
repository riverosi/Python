import sys
import serial
import time
import struct
import numpy as np

#Configure buffers for serial
""" Buffer serial tx size """
BUFFER_SERIAL_TX_SIZE = 512
""" Buffer serial rx size """
BUFFER_SERIAL_RX_SIZE = 512


#Configure baudrate
BAUD_RATE = 460800

expected_footer = bytes((0 , 0 , 0 , 0 , 0 , 0 , 192))

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
        print("Not found Serial Port")
        sys.exit()
    return(serial_devices)

#para convertir de complemento a2 a counts de datos para los 8 canales de eeg
def array_convert(bytes_array):
    counts_channel = []
    counts_channel.append(int.from_bytes(bytes_array[2:4], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[5:7], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[8:10], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[11:13], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[14:16], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[17:19], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[20:22], byteorder='big',signed=True))
    counts_channel.append(int.from_bytes(bytes_array[23:25], byteorder='big',signed=True))
    return counts_channel
    

def read_serial():
    # Serial port obj
    SerialPort = serial.Serial(list_serial_ports(), baudrate=BAUD_RATE, timeout = None)
    #Buffer de entrada y de salida
    SerialPort.set_buffer_size(rx_size = BUFFER_SERIAL_RX_SIZE , tx_size = BUFFER_SERIAL_TX_SIZE)
    print("App is runing!!!")

    while True:
        try:
            buffer_data = SerialPort.read_until(terminator=expected_footer)
            if len(buffer_data) == 33:
                print(array_convert(buffer_data))
                #print(array_convert(struct.unpack('>33B', buffer_data)))
            SerialPort.flush()
        except KeyboardInterrupt:
            #Interrup serial data read whit keyboard interrupt crtl + c
            SerialPort.close()
            print("Keyboard Interrupt")
            break

        
if __name__ == "__main__":
    read_serial()