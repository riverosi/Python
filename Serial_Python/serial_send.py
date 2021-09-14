import sys
import serial
import time
from struct import pack
import numpy as np

#Configure buffers for serial
""" Data size in bytes """
DATA_SIZE = 128
""" Buffer serial tx size """
BUFFER_SERIAL_TX_SIZE = 512
""" Buffer serial rx size """
BUFFER_SERIAL_RX_SIZE = 8


#Configure baudrate
BAUD_RATE = 460800

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


def read_serial( serial_devices ):
    #load data from csv file
    wave_m_csv = np.genfromtxt('m_wave_2khz.csv',delimiter=',')
    data_array = np.zeros(DATA_SIZE - len(wave_m_csv))
    wave_m_sized =np.append(wave_m_csv , data_array)

    SerialPort = serial.Serial(serial_devices, baudrate=BAUD_RATE, timeout = None)
    #Buffer de entrada y de salida
    SerialPort.set_buffer_size(rx_size = BUFFER_SERIAL_RX_SIZE , tx_size = BUFFER_SERIAL_TX_SIZE)
    print("App is runing!!!")

    while True:
        try:
            for element in wave_m_sized:
                #uncomment for print data
                #print(pack('f' , element))
                SerialPort.write(pack('f' , element))
            time.sleep(1.0)
            print("Data packet send...")   
        except KeyboardInterrupt:
            #Interrup serial data read whit keyboard interrupt crtl + c
            SerialPort.close()
            print("Keyboard Interrupt")
            break

    print("End of program")
    return()


if __name__ == "__main__":
    read_serial(list_serial_ports())