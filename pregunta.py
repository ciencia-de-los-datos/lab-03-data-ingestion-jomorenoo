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
    columnas = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave",
    ]
    clusters = []

    with open("clusters_report.txt") as cluster:
        filas = cluster.readlines()[4:]

    for fila in filas:
        if re.match("^ +[0-9]+ +", fila):
            if clusters:
                clusters[-1]["palabras"] = clusters[-1]["palabras"].replace(".", "")
                clusters.append(
                    {
                        "cluster": int(cluster),
                        "cantidad": int(cantidad),
                        "porcentaje": float(porcentaje.replace(",", ".")),
                        "palabras": " ".join(palabras[1:]),
                    }
                )
            else:
                cluster, cantidad, porcentaje, *palabras = fila.split()
                clusters.append(
                    {
                        "cluster": int(cluster),
                        "cantidad": int(cantidad),
                        "porcentaje": float(porcentaje.replace(",", ".")),
                        "palabras": " ".join(palabras[1:]),
                    }
                )
        elif re.match("^ + [a-z]", fila):
            palabras = fila.split()
            clusters[-1]["palabras"] += " " + " ".join(palabras)

    df = pd.DataFrame([list(d.values()) for d in clusters], columns=columnas)
    return df
