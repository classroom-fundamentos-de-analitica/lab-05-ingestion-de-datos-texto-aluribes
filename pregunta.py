"""
Laboratorio 05 - Ingestión de datos textuales
-----------------------------------------------------------------------------------------

Generar dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos archivos deben tener la siguiente estructura:

phrase: Texto de la frase. hay una frase por cada archivo de texto.
sentiment: Sentimiento de la frase. Puede ser "positive", "negative" o "neutral". Este corresponde al nombre del directorio donde se encuentra ubicado el archivo.

"""

# python -m venv .venv
# .venv\Scripts\activate
# python.exe -m pip install --upgrade pip
# pip3 install pyarrow pandas

import os
import csv
import pandas as pd


def create_test_and_train_dataset():
    path = ["/train/", "/test/"]
    output_file = ["train_dataset.csv", "test_dataset.csv"]
    folders = ["negative", "positive", "neutral"]
    i = 0
    for file in output_file:
        with open(file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["phrase", "sentiment"])
        for folder in folders:
            folder_path = "data" + path[i] + folder
            with open(file, "a", newline="") as csvfile:
                writer = csv.writer(csvfile)

                for filename in os.listdir(folder_path):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(folder_path, filename)
                        with open(file_path, "r") as f:
                            content = f.read()
                            writer.writerow([content, folder])
        i += 1
    return


create_test_and_train_dataset()

# df = pd.read_csv('train_dataset.csv')
# print(df["sentiment"].value_counts())


# df2 = pd.read_csv('test_dataset.csv')
# print(df2["sentiment"].value_counts())

