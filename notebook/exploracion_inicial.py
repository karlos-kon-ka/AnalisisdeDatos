# Archivo: exploracion_inicial.py
import pandas as pd

# Leer el dataset desde data/raw/encuesta_madrid.xlsx
df = pd.read_excel('data/raw/encuesta_madrid.xlsx')

# Mostrar las primeras y últimas filas del dataset
print("Primeras filas del dataset:")
print(df.head())
print("\nÚltimas filas del dataset:")
print(df.tail())

# Obtener información general del dataset
print("\nInformación general del dataset:")
print(df.info())

# Guardar el resultado de exploración en un archivo de texto opcionalmente
# df.head().to_csv('reports/exploracion_inicial_resultado.csv', index=False)
