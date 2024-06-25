# Archivo: limpieza_preprocesamiento.py
import pandas as pd
import numpy as np

# Función para tratar valores faltantes NaN y datos fuera de 2 desviaciones típicas
def imputar_valores(df):
    for column in df.columns:
        if df[column].dtype == np.number:
            # Imputar NaN con la media y datos fuera de 2 desviaciones con la moda
            df[column] = df[column].fillna(df[column].mean())
            mean = df[column].mean()
            std_dev = df[column].std()
            upper_limit = mean + 2 * std_dev
            lower_limit = mean - 2 * std_dev
            df[column] = np.where(df[column] > upper_limit, df[column].mode()[0], df[column])
            df[column] = np.where(df[column] < lower_limit, df[column].mode()[0], df[column])
        else:
            # Imputar NaN con la moda
            df[column] = df[column].fillna(df[column].mode()[0])
    return df

# Leer el dataset desde data/raw/dataset.xlsx
df = pd.read_excel('data/raw/dataset.xlsx')

# Aplicar la función de limpieza
df = imputar_valores(df)

# Guardar el dataset limpio en data/processed/dataset_clean.csv
df.to_csv('data/processed/dataset_clean.csv', index=False)
