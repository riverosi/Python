import serial
import csv
from datetime import date, datetime
import serial.tools.list_ports

class serial_reader():
    __BUFFER_SERIAL_TX_SIZE = 512
    __BUFFER_SERIAL_RX_SIZE = 512
    __BAUD_RATE = 460800
    __port_name = ""
    __expected_footer = bytes((0 , 0 , 0 , 0 , 0 , 0 , 192))
    __name_csv_file = "data-" + datetime.today().strftime('%Y-%m-%d-%H%M') + ".csv"

    def list_serial_ports(self):
        try:
            ports = serial.tools.list_ports.comports()
            for port, desc, hwid in sorted(ports):
                if("Serial" in desc):
                    self.__port_name = "{}".format(port)
        except (serial.SerialException , NameError):
            print('Not found Serial Port')
        return(self.__port_name)

    def array_convert(self, bytes_array):
        """
        para convertir de complemento a2 a counts de datos para los 8 canales de eeg
        """
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
    
    def connect(self):
        self.list_serial_ports()
        # Serial port obj
        self.SerialPort = serial.Serial(self.__port_name, baudrate=self.__BAUD_RATE, timeout = None)
        self.file_csv = open(self.__name_csv_file, 'a', newline='')
        self.writer_csv = csv.writer(self.file_csv)
        #Buffer de entrada y de salida
        self.SerialPort.set_buffer_size(rx_size = self.__BUFFER_SERIAL_RX_SIZE , tx_size = self.__BUFFER_SERIAL_RX_SIZE)
        print("App is runing")
        self.SerialPort.reset_input_buffer()

    def disconnect(self):
        self.file_csv.close()
        self.SerialPort.close()
        print("App Interrupt")

    def read(self):
        try:
            buffer_data = self.SerialPort.read_until(terminator=self.__expected_footer, size=33)
            if len(buffer_data) == 33:
                self.writer_csv.writerow(self.array_convert(buffer_data))
        except KeyboardInterrupt:
            self.disconnect()
        return buffer_data

biopot_serial = serial_reader()

if __name__ == "__main__":
    biopot_serial.connect()
    while True:
        biopot_serial.read()