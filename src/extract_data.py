import os
from util import save_data

class ExtractData:
    def get_data(path_file):
        try:
            with open(path_file, 'r') as archivo:
                lineas = archivo.readlines()
            lineas = [linea.strip() for linea in lineas]
            for idx, linea in enumerate(lineas, start=1): 
                print(f"{idx}: {linea}")  
            
        except FileNotFoundError:
            print(f"\nNo existe la ruta {path_file}, o aún no hay datos\n")
            return []
        
      

