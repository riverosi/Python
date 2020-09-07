import csv
#Función para convertir de cadena de bytes a lo que necesitamos
def bytes_to_int(entrada):
    lista = []
    FRS_ACC = 2.0/32767
    FRS_GYR = 250.0/32767
    FRS_MAG = 4800.0/32767
    
    accel_x = (((ord(entrada[0]))<<8) or ord(entrada[1]))*FRS_ACC
    lista.append(accel_x)
    accel_y = (((ord(entrada[2]))<<8) or ord(entrada[3]))*FRS_ACC
    lista.append(accel_y)
    accel_z = (((ord(entrada[4]))<<8) or ord(entrada[5]))*FRS_ACC
    lista.append(accel_z)
    gyro_x = (((ord(entrada[8]))<<8) or ord(entrada[9]))*FRS_GYR
    lista.append(gyro_x)
    gyro_y = (((ord(entrada[10]))<<8) or ord(entrada[11]))*FRS_GYR
    lista.append(accel_y)
    gyro_z = (((ord(entrada[12]))<<8) or ord(entrada[13]))*FRS_GYR
    lista.append(accel_z)

    return lista

#Función para convertir de cadena de bytes a lo que necesitamos
def MPU_Convert(entrada):
    lista = []
    FRS_ACC = 2.0/32767
    FRS_GYR = 250.0/32767
    FRS_MAG = 4800.0/32767
    lista.append(entrada[1]*FRS_ACC)
    lista.append(entrada[2]*FRS_ACC)
    lista.append(entrada[3]*FRS_ACC)
    lista.append(entrada[4]*FRS_GYR)
    lista.append(entrada[5]*FRS_GYR)
    lista.append(entrada[6]*FRS_GYR)
    lista.append(entrada[7]*FRS_MAG)
    lista.append(entrada[8]*FRS_MAG)
    lista.append(entrada[9]*FRS_MAG)
  
    return lista


# Se lee un archivo .txt utilizando la biblioteca "csv"
with open('EDU_CIAA_Data1.txt', 'r', encoding = 'utf_8', newline='\n') as archivo:
    lector_csv = csv.reader(archivo, delimiter=';')
    # for row in lector_csv:
    #     print(row)

print(len(lector_csv))

for linea in lector_csv:
    if  "MPU" in linea:
        linea = MPU_Convert(linea)
        print(linea)

# Trigger = []
# posiciones = 0
# print(len(datos))
# for linea in datos:
#     posiciones += 1
#     if "Trigger" in linea:
#         Trigger.append(int(posiciones))

# print(Trigger)

# datos = datos[Trigger[0]:Trigger[1]-2]

# archivo_MPU1  = open('MPU1.csv','w',encoding = 'utf_8', newline='\n');
# archivo_MPU2  = open('MPU2.csv','w',encoding = 'utf_8', newline='\n');

# for linea in datos:
#     if  "MPU1" in linea:
#         linea = linea.replace("MPU1;", "")
#         print(bytes_to_int(linea))
        
        
#         archivo_MPU1.writelines(linea)
#     # if  "MPU2" in linea:
#     #     linea = linea.replace("MPUSlave", "")
#     #     linea = linea.replace(";", ",")
#     #     linea = linea[1:-1]
#     #     archivo_slave.writelines(linea)
        
# archivo_master.close()
# archivo_slave.close()