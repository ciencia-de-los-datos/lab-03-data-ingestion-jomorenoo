"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra


"""

import re
import pandas as pd


def ingest_data():

    filas = []

    columnas = ["cluster", "key_cant_words", "%_key_words", "principal_key_words"]

    cluster = []

    dictionary = {
        "cluster": 0,
        "cantidad": 0,
        "porcentaje": 0,
        "palabras": "",
    }

    with open("clusters_report.txt") as cluster:
        filas = cluster.readlines()
    filas = filas[4:]

    for fila in filas:
        if re.match("^ +[0-9]+ +", fila):
            cluster, cantidad, porcentaje, *palabras = fila.split()
            dictionary["cluster"] = int(cluster)
            dictionary["cantidad"] = int(cantidad)
            dictionary["porcentaje"] = float(porcentaje.replace(",", "."))
            palabras = " ".join(palabras[1:])

        elif re.match("^ + [a-z]", fila):
            palabras = fila.split()
            palabras = " ".join(palabras)
            dictionary["palabras"] += " " + palabras

        elif re.match("^\n", fila) or re.match("^ +$", fila):
            dictionary["palabras"] = dictionary["palabras"].replace(".", "")
            cluster.append(dictionary.values())

            dictionary = {
                "cluster": 0,
                "cantidad": 0,
                "porcentaje": 0,
                "palabras": "",
            }
    df = pd.DataFrame(cluster, columns=columnas)

    return df
