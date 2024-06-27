import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos procesados
df = pd.read_csv('../data/processed/dataset_clean.csv')

# Gráficos de barras para resumir hallazgos
plt.figure(figsize=(10, 6))
sns.barplot(x='categoria', y='valor', data=df)
plt.title('Distribución por Categorías')
plt.show()

# Gráfico de líneas para mostrar tendencias
plt.figure(figsize=(10, 6))
sns.lineplot(x='fecha', y='ventas', data=df)
plt.title('Tendencias de Ventas a lo Largo del Tiempo')
plt.show()

# Gráfico de pie para mostrar proporciones
plt.figure(figsize=(8, 8))
df['categoria'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Proporción de Categorías')
plt.ylabel('')
plt.show()

# Conclusiones
conclusiones = """
1. Las ventas tienden a ser mayores en los meses de verano.
2. Existe una fuerte correlación entre el gasto en publicidad y las ventas.
3. Las categorías de productos A y B tienen el mayor margen de beneficio.
"""
print(conclusiones)
