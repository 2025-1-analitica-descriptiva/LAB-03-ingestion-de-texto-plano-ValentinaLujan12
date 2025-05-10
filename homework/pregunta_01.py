"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    data = []
    cluster = None
    cantidad = None
    porcentaje = None
    palabras_clave = ""

    for line in lines[4:]: 
        if re.match(r"^\s+\d+", line):  
            if cluster is not None:
                palabras_clave_limpias = re.sub(r"\s+", " ", palabras_clave).strip(" .")
                data.append([cluster, cantidad, porcentaje, palabras_clave_limpias])
            
            cluster = int(line[0:5].strip())
            cantidad = int(line[5:17].strip())
            porcentaje = float(line[17:31].strip().replace(",", ".").replace("%", ""))
            palabras_clave = line[31:].strip()
        else:
            palabras_clave += " " + line.strip()

    if cluster is not None:
        palabras_clave_limpias = re.sub(r"\s+", " ", palabras_clave).strip(" .")
        data.append([cluster, cantidad, porcentaje, palabras_clave_limpias])

    df = pd.DataFrame(data, columns=[
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave"
    ])

    return df

if __name__ == "__main__":
    df = pregunta_01()
    print(df)