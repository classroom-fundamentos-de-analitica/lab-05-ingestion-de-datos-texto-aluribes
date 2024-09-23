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


def create_csv_from_directory(directory, output_file):
    data = []

    for sentiment in ["positive", "negative", "neutral"]:
        sentiment_path = os.path.join(directory, sentiment)
        if os.path.exists(sentiment_path):
            for filename in os.listdir(sentiment_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(sentiment_path, filename)
                    with open(file_path, "r", encoding="utf-8") as file:
                        phrase = file.read().strip()
                        data.append([phrase, sentiment])

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["phrase", "sentiment"])
        writer.writerows(data)


create_csv_from_directory("data/train", "train_dataset.csv")

create_csv_from_directory("data/test", "test_dataset.csv")

# df = pd.read_csv('train_dataset.csv')
# print(df["sentiment"].value_counts())
 
# df2 = pd.read_csv('test_dataset.csv')
# print(df2["sentiment"].value_counts())

