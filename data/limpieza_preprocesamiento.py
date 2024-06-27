import pandas as pd
import matplotlib.pyplot as plt

# Función para imputar valores faltantes
def imputar_valores_faltantes(df):
    for column in df.columns:
        if df[column].isnull().sum() > 0:
            if df[column].dtype == 'float64' or df[column].dtype == 'int64':
                df[column].fillna(df[column].mean(), inplace=True)
            else:
                df[column].fillna(df[column].mode()[0], inplace=True)
    return df

# Cargar el dataset
df = pd.read_excel('/raw/dataset.xlsx')

# Imputar valores faltantes
df = imputar_valores_faltantes(df)

# Guardar datos procesados
df.to_csv('../data/processed/dataset_clean.csv', index=False)

# Comprobar la limpieza
print(df.isnull().sum())

# Histogramas después de la limpieza
df.hist(bins=50, figsize=(20, 15))
plt.show()

# Gráfico de caja para ver los outliers
df.plot(kind='box', subplots=True, layout=(4,4), sharex=False, sharey=False, figsize=(20, 15))
plt.show()
