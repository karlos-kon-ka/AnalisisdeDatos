import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el dataset limpio desde data/processed/dataset_clean.csv
df = pd.read_csv('data/procesado/encuesta_madrid.csv')

# Función para calcular estadísticas básicas
def calcular_estadisticas(df):
    estadisticas = {}
    for column in df.select_dtypes(include=[np.number]).columns:
        estadisticas[column] = {
            'media': df[column].mean(),
            'mediana': df[column].median(),
            'desviacion_estandar': df[column].std()
        }
    return estadisticas

# Calcular estadísticas básicas
print("\nEstadísticas básicas:")
print(calcular_estadisticas(df))

# Crear gráficos para visualización
# Histogramas
df.hist(bins=50, figsize=(20, 15))
plt.savefig('reports/histogramas.png')  # Guardar los histogramas como imagen
plt.close()

# Diagramas de caja
df.plot(kind='box', subplots=True, layout=(4,4), sharex=False, sharey=False, figsize=(20, 15))
plt.savefig('reports/diagramas_caja.png')  # Guardar los diagramas de caja como imagen
plt.close()

# Correlaciones entre variables
correlacion = df.corr()
sns.heatmap(correlacion, annot=True, cmap='coolwarm')
plt.savefig('reports/heatmap_correlacion.png')  # Guardar el heatmap de correlación como imagen
plt.close()