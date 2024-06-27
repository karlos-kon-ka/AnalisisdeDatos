import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_excel('../data/raw/dataset.xlsx')

# Mostrar primeras filas
print(df.head())

# Resumen estadístico
print(df.describe())

# Histograma para cada columna numérica
df.hist(bins=50, figsize=(20, 15))
plt.show()

# Gráfico de calor para ver las correlaciones
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
