# -*- coding: utf-8 -*-


import csv
from datetime import datetime, time, date, timedelta
import traceback
import os
import sys
import json


ARCHIVO_ORIGEN = "partir_archivo_origen.txt"
CANTIDAD_ARCHIVOS = 10

def partir_archivo_origen():

   
    smallfile = None
    cantidad_archivos = CANTIDAD_ARCHIVOS
    num_lines_total = sum(1 for line in open(ARCHIVO_ORIGEN))
    
    total_lineas_archivo = int(num_lines_total / cantidad_archivos )


    with open( ARCHIVO_ORIGEN ,encoding='utf-8') as bigfile:
        print("numero de lineas totales ", num_lines_total )
        print("total lineas por archivo", total_lineas_archivo  )

        
        for lineno, line in enumerate(bigfile):
            if lineno % total_lineas_archivo == 0:
                if smallfile:
                    smallfile.close()
                small_filename = 'destino_archivos/small_file_{}.txt'.format(lineno + total_lineas_archivo)
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        

def main():
    print("iniciando programa partir archivo")
    try:
        
        partir_archivo_origen()
        

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
