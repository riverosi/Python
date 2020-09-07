import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

print("List of connected Devices:")
serial_devices = "No Serial Devices"
for port, desc, hwid in sorted(ports):
        serial_devices = "{}".format(port)
print(serial_devices)


import serial
import time
import csv
from struct import unpack
import numpy as np

def bytes_to_int(entrada):
    arreglo = np.empty(10, dtype = int)
    #Accel Registers
    arreglo[0] = np.int16((entrada[0]<<8) | entrada[1])
    arreglo[1] = np.int16((entrada[2]<<8) | entrada[3])
    arreglo[2] = np.int16((entrada[4]<<8) | entrada[5])
    #Temp Registers
    arreglo[3] = np.int16((entrada[6]<<8) | entrada[7])
    #Gyro Registers
    arreglo[4] = np.int16((entrada[8]<<8) | entrada[9])
    arreglo[5] = np.int16((entrada[10]<<8) | entrada[11])
    arreglo[6] = np.int16((entrada[12]<<8) | entrada[13])
    #Mag Ragisters
    arreglo[7] = np.int16((entrada[15]<<8) | entrada[14])
    arreglo[8] = np.int16((entrada[17]<<8) | entrada[16])
    arreglo[9] = np.int16((entrada[19]<<8) | entrada[18])
    
    return arreglo


def main():
    #Funcion lamba, a la llamada devuelve el tiempo en ms
    current_milli_time = lambda: int(round(time.time() * 1000))
    #Variable de tiempo enlapsado para sincronizar
    time_enlapsed = current_milli_time()

    SerialPort = serial.Serial(serial_devices, baudrate=460800, timeout = None)
    #Buffer de entrada y de salida de 32bytes
    SerialPort.set_buffer_size(rx_size = 32 , tx_size = 32) 
    array_out = np.empty([1,0], dtype=int)

    while True:
        try:
            line = SerialPort.read(size = 22)
            array_out = np.array([current_milli_time() - time_enlapsed], dtype=int) 
            print( np.append( array_out , bytes_to_int(unpack('22B',line)) ) )
            SerialPort.reset_input_buffer()
        except KeyboardInterrupt:
            SerialPort.close()
            print("Keyboard Interrupt")
            break

    print("End of program")
    return()


if __name__ == "__main__":
    main()