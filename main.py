# -*- coding: utf-8 -*-


import csv
from datetime import datetime, time, date, timedelta
import traceback
import os
import sys
import json



# declarar path archivo origen

ARCHIVO_ORIGEN = "archivo_origen.csv"
ARCHIVO_SALIDA = "archivo_salida.csv"
ARCHIVO_SALIDA_ERRORES = "errores.txt"


DELIMITADOR_ARCHIVO = ";"

LISTA_ERRORES = []


def check_date_format(fecha_origen):

    if fecha_origen is not None:

        try:
            datetime.strptime(fecha_origen.strip(), '%d/%m/%Y')    
            fecha_origen = fecha_origen.strip()
            return {"status": True, "date": fecha_origen}
        except ValueError:
            return {"status": False, "date": None}
    else:
        return {"status": False, "date": None}


def read_file_csv():
    nuevo_array_fila = []
    nuevo_archivo_list = []
    with open(ARCHIVO_ORIGEN, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=DELIMITADOR_ARCHIVO)
        contador_lineas = 0
        for fila_archivo in csv_reader:
            a = 0
            if contador_lineas > 0:
                nuevo_array_fila = []
                nuevo_array_fila = fila_archivo
                if len(fila_archivo) > 3:
                    
                    valiacion_fecha = check_date_format(fila_archivo[2])
                    nueva_fecha = ""
                    if valiacion_fecha["status"] == True:
                        nueva_fecha = valiacion_fecha["date"]
                    else:
                        nueva_fecha = "ERROR_FORMATO_FECHA"

                        error_fecha = "En la fila " + str( int(contador_lineas + 1) ) + " el formato de fecha es no válido," + str(fila_archivo[0]) +","+str(fila_archivo[2])

                        LISTA_ERRORES.append(error_fecha)
                    nuevo_array_fila[2] = nueva_fecha
                    nuevo_archivo_list.append(nuevo_array_fila)
                    # se valida la columna fecha
                    

            
            contador_lineas = contador_lineas + 1

        
        contador_filar = 0
        for fila_archivo_nuevo in nuevo_archivo_list:
            
            fecha = fila_archivo_nuevo[2]
            #print("contador_filar",contador_filar)

            #print((fecha))

            #print((fecha).encode('utf-8').strip())
            contador_filar = contador_filar + 1
            #print(fecha)

        crear_archivo_salida(nuevo_archivo_list)

def crear_archivo_salida(registros):
    fields = [('Radicacion_fs').upper(), ('NroItem').upper(), ("Fecha fallo").upper(),('Número de fallo').upper(), ('Motivo').upper(),("Resuelve").upper(),("Observaciones").upper()]
    with open(ARCHIVO_SALIDA, 'w' , encoding='utf-8') as f: 
        write = csv.writer(f) 
        write.writerow(fields) 
        write.writerows(registros) 


    with open(ARCHIVO_SALIDA_ERRORES, 'w',  encoding='utf-8') as f:
        for item in LISTA_ERRORES:
            f.write("%s\n" % item)





def main():
    print("iniciando reparacion archivo")
    try:
        read_file_csv()

    except Exception as error:
          error_msg = traceback.format_exc()
          status_create = False
          
          exc_type, exc_obj, exc_tb = sys.exc_info()
          fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
          
          line_error = exc_tb.tb_lineno
          status_create = False
          module_path = sys.modules[__name__]

          error_object = {

              "msg": error_msg,
              "line": line_error,
              "module": module_path
          }

          print(error_object)

if __name__ == "__main__":
    main()