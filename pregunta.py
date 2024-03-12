"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""

import pandas as pd


def ingest_data():
    # Defino el archivo como variable y lo leo
    archivo = "clusters_report.txt"

    with open(archivo, "r") as f:
        lineas = f.readlines()

    data = []
    for line in lineas:

        words = line.strip().split()
        keywords = ", ".join(words[3:])

        row = {
            "cluster_id": words[0],
            "cluster_size": words[1],
            "centroid": words[2],
            "keywords": keywords,
        }
        data.append(row)

    df = pd.Dataframe(data)
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    return df
